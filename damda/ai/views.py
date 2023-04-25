from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.http import StreamingHttpResponse
from django.views import generic
from django.template.loader import get_template 
from django.urls import reverse
from random import randint

import cv2, time
import threading

from .models import Dam


def index(request):
    context = {
      "bg_type": randint(0,7)
    }
    return render(request, "index.html", context)


def name_form(request):
    if request.method == "POST":
        username = request.POST.get('username')
        if username != '':
            request.session['username'] = username
            return redirect('ai:name-result')

    return render(request, "name_form.html")


def name_result(request):
    context = {
      "username": request.session.get('username')
    }
    return render(request, "name_result.html", context)


def face(request):
    template = get_template('face.html')
    return HttpResponse(template.render({}, request))


def stream():
    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: failed to capture image")
            break

        cv2.imwrite('demo.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg', 'rb').read() + b'\r\n')


def video(request):
        try:
            time.sleep(2)
            return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')
        except HttpResponseServerError as e:
            print("asborted", e)