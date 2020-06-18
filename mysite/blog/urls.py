from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:artcle_title>', views.detail, name='detail'),


]