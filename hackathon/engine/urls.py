from django.contrib import admin
from django.urls import path,include
from engine import views

urlpatterns = [
    
    path('', views.root,name="root"),
    path('add/', views.add,name="add"),
    path('search/', views.search,name="search"),
    path('force/', views.force,name="force"),
    path('force-add/', views.forceadd,name="forceadd"),
    path('search/email-lost/<int:slug>', views.emailLost,name="email"),
    path('add/email-found/<int:slug>', views.emailf,name="emailf"),
    
]