from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='home'),
    path('example/', views.example, name='example')

]