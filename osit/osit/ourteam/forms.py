from django import forms
from tinymce.widgets import TinyMCE
from .models import Ourteam, Teammember

class NewTeamForm(forms.ModelForm):

    class Meta:
        model = Ourteam
        fields = ['name']

class NewMemberForm(forms.ModelForm):
    details = forms.CharField(
        widget=TinyMCE(attrs={'class': 'tinymce-editor'}),
        max_length=4000,
        help_text='The max length of the text is 4000.'
        )
    
    
    image = forms.ImageField(label='Upload Image', required=False) 

    class Meta:
        model = Teammember
        fields = ['name', 'details', 'image']
        widgets = {
            'details': TinyMCE(),
        }