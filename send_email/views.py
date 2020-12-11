from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .form import NameForm

# Create your views here.


def send_email(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_to = form.cleaned_data['send_to']
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            send_mail(subject, message, settings.EMAI_HOST_USER, [send_to])
            return redirect("/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})
