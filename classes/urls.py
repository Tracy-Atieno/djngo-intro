from django.urls import path

from classes import views

app_name ='classes'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.about, name="about")

]
