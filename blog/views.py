from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class Dashboard(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "dashbord.html"