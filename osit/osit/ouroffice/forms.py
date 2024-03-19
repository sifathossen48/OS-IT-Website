from django import forms
from tinymce.widgets import TinyMCE
from .models import Ouroffice

class NewOfficeForm(forms.ModelForm):
    details = forms.CharField(
        widget=TinyMCE(attrs={'class': 'tinymce-editor'}),
        max_length=4000,
        help_text='The max length of the text is 4000.'
        )
    
    

    class Meta:
        model = Ouroffice
        fields = ['name', 'details']
        widgets = {
            'details': TinyMCE(),
        }