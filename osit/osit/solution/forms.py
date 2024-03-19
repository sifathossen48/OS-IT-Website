from django import forms
from .models import Solution, Product
from multiupload.fields import MultiFileField

class NewSolutionForm(forms.ModelForm):

    class Meta:
        model = Solution
        fields = ['name']


class NewProductForm(forms.ModelForm):
    
    image = forms.ImageField(label='Upload Image', required=False) 
    """ image = MultiFileField(min_num=1, max_num=10, required=False, label='Upload Images') """

    class Meta:
        model = Product
        fields = ['name', 'image']


   


   

