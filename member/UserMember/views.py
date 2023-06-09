from django.shortcuts import render, redirect
from .forms import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import paho.mqtt.client as mqtt
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
            return redirect('UserMember:controlPage')
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
client = mqtt.Client("bangled")
client.username_pw_set("bangled", "bangled")
def on_message(mqtt_client, userdata, msg):
   print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
if client.connect("aiot-jsc1.ddns.net", 1889, 60) != 0:
    print("Could not connect  to MQTT Broker")
    sys.exit(-1)
client.publish("django/mqtt_pub", "Hello Broker123", 1)


class sendMQTT(LoginRequiredMixin, View):
    login_url = '/login/'
    def post(self, request):
        textCt = request.POST['textCt']
        speedCt = request.POST['speedCt']
        row = request.POST['row']
        json_data = {
            "textCt": textCt,
            "speedCt" : speedCt,
            "row": row,
        }
        package_data = json.dumps(json_data)
        client.publish("django/mqtt_pub", package_data, 1)
        return render(request, 'UserMember/control.html')
    client.loop_start()
def postMQTT(request):
    if request.method == 'POST':
        status = request.POST['status']
        led = request.POST['led']
        success = "Success"
        return HttpResponse(success)

class controlPage(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'UserMember/control.html')


