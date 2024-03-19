from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ouroffice
from .forms import NewOfficeForm
from django.views.generic import UpdateView

"""ouroffice view"""

def ouroffice(request):
    ouroffice = Ouroffice.objects.all()
    return render(request, 'ouroffice.html', {'ouroffice': ouroffice})

"""new_office view"""

def new_office(request):
    if request.method == 'POST':
        form = NewOfficeForm(request.POST, request.FILES)
        if form.is_valid():
            ouroffice = form.save(commit=False)

            ouroffice.details = form.cleaned_data['details']

            ouroffice.save()
            
            return redirect('ouroffice')
        
    else:
        form = NewOfficeForm()
    return render(request, 'new_office.html', {'form': form})


"""particular_office view"""

def particular_office(request, pk):
    ouroffice = get_object_or_404(Ouroffice, pk=pk)

    return render(request, 'particular_office.html', {'ouroffice': ouroffice})


"""OfficeUpdateView class"""

class OfficeUpdateView(UpdateView):
    model = Ouroffice
    fields = ('name', 'details')
    template_name = 'edit_office.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'ouroffice'

    def form_valid(self, form):
        ouroffice = form.save(commit=False)

        ouroffice.save()
        return redirect('particular_office', pk=ouroffice.pk)