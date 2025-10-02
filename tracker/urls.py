from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracker_view, name='tracker'),
    path('tracker/<slug:slug>/', views.tracker_view, name='tracker_detail'),
    path('tracker/log/', views.cycle_log_form_view, name='cycle_log_form'),
    path('submit-log/', views.submit_log, name='submit_log'),
    path('export.csv', views.export_entries_csv, name='export_csv'),
    path('journey/', views.journey, name='journey'),
]