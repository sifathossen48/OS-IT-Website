from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import CareerForm

"""careerView view"""

def careerView(request):
    if request.method == "GET":
        form = CareerForm()
    else:
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            from_email = form.cleaned_data["from_email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data['message']
            cv = request.FILES.get('cv')

            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=["info@ositsltd.com"],
            )

            # Attach the CV file to the email if it exists
            if cv:
                email.attach(cv.name, cv.read(), cv.content_type)

            try:
                email.send(fail_silently=False)
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("success")

    return render(request, "career.html", {"form": form})


"""successView view"""

def successView(request):
    return HttpResponse("Success! Thank you for your message.")