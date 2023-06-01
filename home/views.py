from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    # return HttpResponse("this is homepage")
    context={
        'variable':"this is variable date sent from views"
    }
    return render(request,'index.html',context)


def about(request):
    # return HttpResponse("this is about page")
    return render(request,'about.html')

def services(request):
    return HttpResponse("this is service page")
    # return render(request,'index.html')

def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, "your message is sent.")

    return render(request,'contact.html')