from django.shortcuts import render, HttpResponse
from Code.models import Black
from Code.models import White
from django.contrib import messages 
from Code.models import Contact

# Create your views here.
def index(request):
    allWhites = White.objects.all()
    allBlacks = Black.objects.all()
    context = {'allBlacks': allBlacks, 'allWhites': allWhites}
    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        description = request.POST.get("description")
        contact = Contact(name=name, email=email, subject=subject, description=description)
        contact.save()
        messages.success(request, "Your message has been sent successfully")
    return render(request, 'contact.html')