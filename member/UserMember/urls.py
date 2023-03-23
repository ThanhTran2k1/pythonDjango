from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'UserMember'
urlpatterns = [

    path('register/', views.registerUser.as_view(), name = 'registerUser'),
    path('', views.loginUser.as_view(), name = 'loginUser'),
    path('logout/', views.logoutUser.as_view(), name = 'logoutUser'),
    path('private/', views.privatePage.as_view(), name = 'privatePage'),
    path('sendMQTT/', views.sendMQTT.as_view(), name = 'sendMQTT'),
    path('publishMQTT/', views.publishMQTT.as_view(), name = 'publishMQTT'),
]