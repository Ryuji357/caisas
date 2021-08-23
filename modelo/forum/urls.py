from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastrar, name='cadastrar'),
    path('ini_thread/', views.ini_thread, name='ini_thread'),
]