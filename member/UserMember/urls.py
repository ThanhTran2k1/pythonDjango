from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'UserMember'
urlpatterns = [

    path('register/', views.registerUser.as_view(), name = 'registerUser'),
    path('', views.loginUser.as_view(), name = 'loginUser'),
    path('logout/', views.logoutUser.as_view(), name = 'logoutUser'),
    path('private/', views.privatePage.as_view(), name = 'privatePage'),
    path('control/', views.controlPage.as_view(), name = 'controlPage'),
    path('sendMQTT/', views.sendMQTT.as_view(), name = 'sendMQTT'),
]
