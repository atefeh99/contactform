from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    if request.method == "POST":
        message = request.POST['message']
        to = 'mahbobe.9495@gmail.com'
        send_mail(
            'Contact_Form',
            message,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently=False)
            
    return render(request,"contactform/index.html",{})