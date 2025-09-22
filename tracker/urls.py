from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracker_view, name='tracker'),
    path('tracker/', views.tracker_view, name='tracker'),
    path('tracker/<slug:slug>/', views.tracker_view, name='tracker_detail'),
]