from django.shortcuts import render
from .models import Post, Event 
from documents.models import DocModel
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, 'home.html')

@login_required
def bulletin(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'bulletin.html', {'posts':posts})

@login_required
def events(request):
    list = Event.objects.all().order_by('date_of')
    return render(request, "events.html", {"list":list})