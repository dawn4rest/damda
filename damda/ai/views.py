from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse, StreamingHttpResponse
from django.template.loader import render_to_string

import random
import cv2, time
import threading

from ai.find_problem import find_problem
from ai.face_predict import face_prediction


def index(request):
    return render(request, 'index.html')


def name_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username != '':
            request.session['username'] = username
            return redirect('ai:name-result')

    return render(request, 'name_form.html')


def name_result(request):
    request.session['red'] = 0
    request.session['green'] = 0
    request.session['blue'] = 0
    request.session['quizStage'] = 1
    request.session['quizPoint'] = 0
    return render(request, 'name_result.html')


def feel_form(request):
    if request.method == 'POST':
        feel = request.POST.get('feel')
        if feel != '':
            request.session['feel'] = feel

    return HttpResponse(status=204)


def feel_result(request):
    return render(request, 'feel_result.html')


def quiz_form(request):
    quizValue = {
      1: [0, -1, 1],
      2: [-1, 1, 0],
      3: [1, 0, -1],
      4: [0, 1, -1],
      5: [-1, 1, 0],
      6: [1, 0, -1],
      7: [-1, 0, 1],
      8: [1, -1, 0],
      9: [1, 0, -1],
      10: [1, -1, 0],
    }

    if request.method == 'POST':
        quizPoint = request.POST.get('quizPoint')
        if quizPoint is not None and request.session['quizStage'] < 11:
            request.session['quizStage'] = request.session['quizStage'] + 1
            request.session['quizPoint'] = request.session['quizPoint'] +int(quizPoint)
            return HttpResponse(status=204)

    context = {'quizValue': quizValue}
    return render(request, 'quiz_form.html', context)


def quiz_result(request):
    soloType = [2, 5, 9]
    soloObj = {
      2: {1: '달', 2: '사람얼굴', 3: '나비'},
      5: {1: '여성', 2: '나무', 3: '그외'},
      9: {1: '입술', 2: '나무', 3: '뿌리'},
    }
    quizScript = {
      1: '다음 그림 중 가장 마음에 드는 그림을 골라주세요.',
      2: '다음 그림에서 무엇이 먼저 보이시나요?',
      3: '다음 그림 중 가장 행복해 보이는 그림을 고르세요.',
      4: '다음 그림 중 인간관계를 가장 잘 표현한 그림은 무엇인가요?',
      5: '다음 그림에서 무엇이 먼저 보이시나요?',
      6: '다음 사진 중 가장 힘들어 보이는 사람은 누구인가요?',
      7: '다음 사진 중 평소 당신의 표정은 어떤가요?',
      8: '다음 사진 중 가장 마음에 드는 생일 날 사진은 무엇인가요?',
      9: '다음 그림에서 무엇이 먼저 보이시나요?',
      10: '가장 마음에 드는 그림을 골라주세요.',

    }
    
    if request.session['quizStage'] in soloType:
      quizType = 'solo'
    else:
      quizType = 'triple'

    context = {
      'quizType': quizType,
      'soloObj': soloObj,
      'quizScript': quizScript,
    }
    return render(request, 'quiz_result.html', context)


def problem_form(request):
    if request.method == 'POST':
        problem = request.POST.get('problem')
        problem_result = find_problem(problem)
        if problem_result != '':
            request.session['problem'] = problem
            request.session['problem_result'] = problem_result
        return HttpResponse(status=204)

    return render(request, 'problem_form.html')


def problem_result(request):
    return render(request, 'problem_result.html')


def face01_form(request):
    answer , red, green, blue = face_prediction('./ai/best_model(cpu).pkl',r'./ai/haarcascade_frontalface_default.xml')

    request.session['red'] = red
    request.session['green'] = green
    request.session['blue'] = blue

    if answer == 'positive':
      request.session['emotion01'] = True
    else: 
      request.session['emotion01'] = False

    return render(request, 'face01_form.html')


def face01_result(request):
    return render(request, 'face01_result.html')


def face02_form(request):
    answer , red, green, blue = face_prediction('./ai/best_model(cpu).pkl',r'./ai/haarcascade_frontalface_default.xml')

    request.session['red'] = red
    request.session['green'] = green
    request.session['blue'] = blue

    if answer == 'positive':
      request.session['emotion02'] = True
    else: 
      request.session['emotion02'] = False
    return render(request, 'face02_form.html')


def face02_result(request):
    return render(request, 'face02_result.html')


def draw_form(request):
    return render(request, 'draw_form.html')


def draw_result(request):
    return render(request, 'draw_result.html')


def result(request):
    return render(request, 'result.html')


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