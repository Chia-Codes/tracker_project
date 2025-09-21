from . import views
from django.urls import path

urlpatterns = [
    path('', views.Dashboard.as_view(), name='home'),
]