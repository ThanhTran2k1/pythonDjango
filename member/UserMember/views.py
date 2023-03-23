from django.shortcuts import render, redirect
from .forms import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import paho.mqtt.client as paho
import sys
import json

# Create your views here.
class registerUser(View):
    def get(self, request):
        rF = registerForm
        return render(request, 'UserMember/register.html', {'rF': rF})

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPass = request.POST["repeatPass"]

        if password == repeatPass:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('UserMember:loginUser')
        else:
            return redirect('UserMember:registerUser')


class loginUser(View):
    def get(self, request):
        lF = loginForm
        return render(request, 'UserMember/login.html', {'lF': lF})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('UserMember:privatePage')
        else:
            return redirect('UserMember:loginUser')


class logoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('UserMember:loginUser')


class privatePage(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'UserMember/private.html')


# MQTT
client = paho.Client()
if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect  to MQTT Broker")
    sys.exit(-1)
client.publish("django/mqtt", "Hello Broker", 0)


class sendMQTT(LoginRequiredMixin, View):
    login_url = '/login/'
    def post(self, request):
        status = request.POST['status']
        led = request.POST['led']
        json_data = {
            "led": led,
            "status" : status,
        }
        package_data = json.dumps(json_data)
        client.publish("django/mqtt", package_data, 0)
        return render(request, 'UserMember/private.html')
