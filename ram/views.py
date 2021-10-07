from django.shortcuts import render,HttpResponse
from datetime import datetime
from ram.models import contactInfo
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    

def images(request):
    return render(request, 'images.html')

# def service(request):
#     return render(request, 'service.html')

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = contactInfo(name=name, email=email, phone = phone, desc = desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has bee submit!')

    return render(request, 'contact.html')
