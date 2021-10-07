from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from ram import views

urlpatterns = [
    path('', views.index, name="home"),
    path('images', views.images, name="images"),
    # path('service', views.service, name="service"),
    path('contact', views.contact, name="contact"),

]