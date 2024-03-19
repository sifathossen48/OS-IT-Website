from django import forms
from .models import News
from multiupload.fields import MultiFileField

class NewNewsForm(forms.ModelForm):
    details = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is new?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    image = forms.ImageField(label='Upload Image', required=False) 
    """ image = MultiFileField(min_num=1, max_num=10, required=False, label='Upload Images') """

    class Meta:
        model = News
        fields = ['title', 'details', 'image']

   


