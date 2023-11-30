from django.shortcuts import render
from django.http import HttpResponse
from .models import User
def home(request):
   return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        subject = request.POST['subject']
        user = User.objects.create(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,subject=subject)
        user.save()
        return render(request, "contact.html")
    else:
        return render(request, 'contact.html')