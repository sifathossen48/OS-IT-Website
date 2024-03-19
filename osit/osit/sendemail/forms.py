from django import forms

class ContactForm(forms.Form):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)