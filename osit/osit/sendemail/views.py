from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


"""contactView view"""

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data["firstName"]
            lastName = form.cleaned_data["lastName"]
            from_email = form.cleaned_data["from_email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["info@ositsltd.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")
    return render(request, "email.html", {"form": form})


"""successView view"""

def successView(request):
    return HttpResponse("Success! Thank you for your message.")