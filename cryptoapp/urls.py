from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('prices/',views.prices,name="prices"),
     path("contact/",views.contact, name = 'ContactUs'),
]
