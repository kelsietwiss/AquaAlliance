from django.shortcuts import render
from .models import DocModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def documents(request):
    list = DocModel.objects.all().order_by('title')
    return render(request, "documents.html", {"list":list})

