from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home , name='damda-home'),
    path('face/', views.face, name='face' ),
    path('video', views.video, name='video'),
    # ex: /ai/
    path("", views.index, name="index"),
    # ex: /ai/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /ai/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /ai/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)