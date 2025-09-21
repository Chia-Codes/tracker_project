from . import views
from django.urls import path

urlpatterns = [
    path('', views.Post.as_view(), name='home'),
]