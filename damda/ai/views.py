from django.shortcuts import render, redirect ,HttpResponse
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import cv2, time

import threading

from django.template.loader import get_template 

def index(request):
    return HttpResponse('Index Page')
    
def home(request):
    return render(request, 'home.html')

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