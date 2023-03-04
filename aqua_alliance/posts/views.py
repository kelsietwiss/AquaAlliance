from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.


def home_view(request):
    form = Post()


def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'post_list.html', {'posts':posts})