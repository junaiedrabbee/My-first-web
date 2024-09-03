from django.shortcuts import render
from Home.models import Contact

def home(request):
    context = {
        "variable": "this is what"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        contact_instance = Contact(name=name, email=email, phone=phone, messages=message)
        contact_instance.save()
        
        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')
