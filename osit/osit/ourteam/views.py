from django.shortcuts import render, get_object_or_404, redirect
from .models import Ourteam, Teammember
from .forms import NewTeamForm, NewMemberForm
from django.views.generic import UpdateView
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

"""ourteam view"""

def ourteam(request):
    ourteam = Ourteam.objects.all()
    return render(request, 'ourteam.html', {'ourteam': ourteam})

"""new_team view"""

def new_team(request):
    if request.method == 'POST':
        form = NewTeamForm(request.POST, request.FILES)
        if form.is_valid():
            ourteam = form.save(commit=False)

            ourteam.name = form.cleaned_data['name']

            ourteam.save()
            
            return redirect('ourteam')
        
    else:
        form = NewTeamForm()
    return render(request, 'new_team.html', {'form': form})



"""ourteam_teammember view"""

def ourteam_teammember(request, pk, teammember_pk=None):
    ourteam = get_object_or_404(Ourteam, pk=pk)

    if teammember_pk:
        teammember = get_object_or_404(Teammember, ourteam__pk=pk, pk=teammember_pk)
        return render(request, 'individual_member.html', {'teammember': teammember})

    # If teammember_pk is not provided, show the list of team members
    teammembers = ourteam.teammember.all()
    return render(request, 'members.html', {'ourteam': ourteam, 'teammembers': teammembers})


"""new_member view"""
    
def new_member(request, pk):
    ourteam = get_object_or_404(Ourteam, pk=pk)
    if request.method == 'POST':
        form = NewMemberForm(request.POST, request.FILES)
        if form.is_valid():
            teammember = form.save(commit=False)
            teammember.ourteam = ourteam
            teammember.details = form.cleaned_data['details']

            teammember.save()
            
            return redirect('individual_member', pk=pk, teammember_pk=teammember.pk)
        
    else:
        form = NewMemberForm()
    return render(request, 'new_member.html', {'ourteam': ourteam, 'form': form})


"""individual_member view"""

def individual_member(request, pk, teammember_pk):
    teammember = get_object_or_404(Teammember, ourteam__pk=pk, pk=teammember_pk)

    teammember.save()
    

    return render(request, 'individual_member.html', {'teammember': teammember})


"""MemberUpdateView class"""

class MemberUpdateView(UpdateView):
    model = Teammember
    fields = ('name', 'details', 'image')
    template_name = 'edit_member.html'
    pk_url_kwarg = 'teammember_pk'
    context_object_name = 'teammember'

    def form_valid(self, form):
        teammember = form.save(commit=False)

        # Handle the image upload
        image_file = self.request.FILES.get('image')
        if image_file:
            # If there's a new image, save it to the model
            teammember.image.save(image_file.name, ContentFile(image_file.read()), save=False)

        teammember.save()
        return redirect('ourteam_teammember', pk=teammember.ourteam.pk, teammember_pk=teammember.pk)
    
    
"""delete_member view"""

def delete_member(request, pk, teammember_pk):
    if request.method == 'POST':
        teammember = get_object_or_404(Teammember, ourteam__pk=pk, pk=teammember_pk)
        teammember.delete()
        return JsonResponse({'message': 'Member deleted successfully'})
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'message': 'Invalid request method'}, status=400)
