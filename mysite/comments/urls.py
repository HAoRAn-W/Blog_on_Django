from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/blog/<int:pk>/', views.blog_comment, name='blog_comment')

]