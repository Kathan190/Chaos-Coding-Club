from django.shortcuts import render, HttpResponse
from Code.models import Black
from Code.models import White

# Create your views here.
def index(request):
    allWhites = White.objects.all()
    allBlacks = Black.objects.all()
    context = {'allBlacks': allBlacks, 'allWhites': allWhites}
    return render(request, 'index.html', context)