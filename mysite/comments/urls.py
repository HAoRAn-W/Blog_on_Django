from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('blog/comment/<int:pk>/', views.blog_comment, name='comment')

]