from django import forms
from .models import Clients
from multiupload.fields import MultiFileField

class NewClientForm(forms.ModelForm):
    
    image = forms.ImageField(label='Upload Client Logo', required=False) 
    """ image = MultiFileField(min_num=1, max_num=10, required=False, label='Upload Images') """

    class Meta:
        model = Clients
        fields = ['image']
