from django.shortcuts import render, get_object_or_404, redirect
from .models import Solution, Product
from .forms import NewSolutionForm, NewProductForm
from django.views.generic import UpdateView
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

"""solution view"""

def solution(request):
    solution = Solution.objects.all()
    return render(request, 'solution.html', {'solution': solution})

"""new_solution view"""

def new_solution(request):
    if request.method == 'POST':
        form = NewSolutionForm(request.POST, request.FILES)
        if form.is_valid():
            solution = form.save(commit=False)

            solution.name = form.cleaned_data['name']

            solution.save()
            
            return redirect('solution')
        
    else:
        form = NewSolutionForm()
    return render(request, 'new_solution.html', {'form': form})


"""solution_product view"""

def solution_product(request, pk, product_pk=None):
    solution = get_object_or_404(Solution, pk=pk)

    if product_pk:
        product = get_object_or_404(Product, solution__pk=pk, pk=product_pk)
        return render(request, 'specific_product.html', {'product': product})

    # If product_pk is not provided, show the list of product
    product = solution.product.all()
    return render(request, 'products.html', {'solution': solution, 'product': product})


"""new_product view"""
    
def new_product(request, pk):
    solution = get_object_or_404(Solution, pk=pk)
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.solution = solution

            product.save()
            
            return redirect('specific_product', pk=pk, product_pk=product.pk)
        
    else:
        form = NewProductForm()
    return render(request, 'new_product.html', {'solution': solution, 'form': form})


"""specific_product view"""

def specific_product(request, pk, product_pk):
    product = get_object_or_404(Product, solution__pk=pk, pk=product_pk)

    product.save()
    

    return render(request, 'specific_product.html', {'product': product})


"""ProductUpdateView class"""

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'image')
    template_name = 'edit_product.html'
    pk_url_kwarg = 'product_pk'
    context_object_name = 'product'

    def form_valid(self, form):
        product = form.save(commit=False)

        # Handle the image upload
        image_file = self.request.FILES.get('image')
        if image_file:
            # If there's a new image, save it to the model
            product.image.save(image_file.name, ContentFile(image_file.read()), save=False)

        product.save()
        return redirect('solution_product', pk=product.solution.pk, product_pk=product.pk)
    
    
"""delete_product view"""

def delete_product(request, pk, product_pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, solution__pk=pk, pk=product_pk)
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'})
    else:
        # Handle other HTTP methods if needed
        return JsonResponse({'message': 'Invalid request method'}, status=400)
