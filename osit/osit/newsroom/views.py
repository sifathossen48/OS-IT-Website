from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewNewsForm
from .models import News
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView
from django.utils import timezone
from django.core.files.base import ContentFile
from django.http import JsonResponse



"""newsroom view"""

def newsroom(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})


"""new_news view"""

def new_news(request):
    if request.method == 'POST':
        form = NewNewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)

            default_user = User.objects.get(username='admin') 
            news.starter = default_user
            # news.starter=request.user
            news.details = form.cleaned_data['details']

            news.save()
            
            return redirect('newsroom')
        
    else:
        form = NewNewsForm()
    return render(request, 'new_news.html', {'form': form})


"""particular_news view"""

def particular_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.views += 1
    news.save()
    

    return render(request, 'particular_news.html', {'news': news})


"""NewsUpdateView class"""

class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'details', 'image')
    template_name = 'edit_news.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'news'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.updated_by = self.request.user
        news.last_updated = timezone.now()
        news.updated_at = timezone.now()

        # Handle the image upload
        image_file = self.request.FILES.get('image')
        if image_file:
            # If there's a new image, save it to the model
            news.image.save(image_file.name, ContentFile(image_file.read()), save=False)

        news.save()
        return redirect('particular_news', pk=news.pk)
    

"""delete_news view"""

def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return JsonResponse({'message': 'News deleted successfully'})
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'message': 'Invalid request method'}, status=400)
