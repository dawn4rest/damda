from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings


app_name = "ai"
urlpatterns = [
    path('', views.index, name='index'),
    path('name-form/', views.name_form, name='name-form'),
    path('name-result/', views.name_result, name='name-result'),
    path('feel-form/', views.feel_form, name='feel-form'),
    path('feel-result/', views.feel_result, name='feel-result'),
    path('quiz-form/', views.quiz_form, name='quiz-form'),
    path('quiz-result/', views.quiz_result, name='quiz-result'),
    path('problem-form/', views.problem_form, name='problem-form'),
    path('problem-result/', views.problem_result, name='problem-result'),
    path('face01-form/', views.face01_form, name='face01-form'),
    path('face01-result/', views.face01_result, name='face01-result'),
    path('face02-form/', views.face02_form, name='face02-form'),
    path('face02-result/', views.face02_result, name='face02-result'),
    path('draw-intro/', views.draw_intro, name='draw-intro'),
    path('draw-result/', views.draw_result, name='draw-result'),
    path('video', views.video, name='video'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)