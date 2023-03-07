from django.shortcuts import render
from .models import DocModel

# Create your views here.

def documents(request):
    list = DocModel.objects.all().order_by('-published_date')
    return render(request, "documents.html", {"list":list})

