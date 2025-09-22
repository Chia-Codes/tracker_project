from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.PostList.as_view(), name='post_detail'),
    path("post/<slug:slug>/", views.post_detail, name="post_detail"),
]