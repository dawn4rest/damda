from django.shortcuts import render, redirect, HttpResponse
from django.http import StreamingHttpResponse

import random
import cv2, time
import threading


def index(request):
    request.session['red'] = 255
    request.session['green'] = 255
    request.session['blue'] = 255
    context = {'bg_type': random.randint(0,7)}
    return render(request, 'index.html', context)


def name_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username != '':
            request.session['username'] = username
            return redirect('ai:name-result')

    return render(request, 'name_form.html')


def name_result(request):
    context = {'username': request.session.get('username')}
    return render(request, 'name_result.html', context)


def name_result(request):
    context = {'username': request.session.get('username')}
    return render(request, 'name_result.html', context)


def feel_form(request):
    return render(request, 'feel_form.html')


def feel_result(request):
    context = {'username': request.session.get('username')}
    return render(request, 'feel_result.html', context)


def problem_form(request):
    if request.method == 'POST':
        problem = request.POST.get('problem')
        if problem != '':
            request.session['problem'] = problem
            return redirect('ai:problem-result')

    return render(request, 'problem_form.html')


def problem_result(request):
    return render(request, 'problem_result.html')


def face01_form(request):
    return render(request, 'face01_form.html')


def face01_result(request):
    request.session['red'] = random.randint(0,255)
    request.session['green'] = random.randint(0,255)
    request.session['blue'] = random.randint(0,255)

    request.session['emotion01'] = random.choice([True, False])
    context = {'emotion01': request.session['emotion01']}
    return render(request, 'face01_result.html', context)


def goal_form(request):
    return render(request, 'goal_form.html')


def goal_result(request):
    return render(request, 'goal_result.html')


def face02_form(request):
    return render(request, 'face02_form.html')


def face02_result(request):
    request.session['red'] = random.randint(0,255)
    request.session['green'] = random.randint(0,255)
    request.session['blue'] = random.randint(0,255)

    request.session['emotion02'] = random.choice([True, False])
    context = {
      'emotion01': request.session['emotion01'],
      'emotion02': request.session['emotion02']
    }
    return render(request, 'face02_result.html', context)


def canvas_intro(request):
    return render(request, 'canvas_intro.html')


def canvas_result(request):
    context = {
      'hex_color': '%02x%02x%02x' % (request.session['red'],request.session['green'],request.session['blue']),
      'quote_index': random.randint(0,56)
    }
    return render(request, 'canvas_result.html', context)


def stream():
    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()

        if not ret:
            print('Error: failed to capture image')
            break

        cv2.imwrite('demo.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg', 'rb').read() + b'\r\n')


def video(request):
        try:
            time.sleep(2)
            return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')
        except HttpResponseServerError as e:
            print('asborted', e)