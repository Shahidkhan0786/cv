from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Contact
from cv import settings
from django.core.mail import send_mail
# Create your views here.

def home(request):
    print("hoi=")
    return render(request , 'info/home.html')

def hire(request):
    if request.method=="POST":
        company = request.POST['company']
        message = request.POST['message']
        contact = Contact(company=company , message=message)
        contact.save()
        try:
            send_mail(
                company,
                message,
                settings.EMAIL_HOST_USER,
                ['shahidkhan0085200@gmail.com'],

            )
        except:
            return redirect('/send')
        return redirect('/send')
    return render(request , 'info/hire.html')

def sent(request):
    return render(request , 'info/skills.html')