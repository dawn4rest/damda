from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home , name='damda-home'),
    path('face/', views.face, name='face' ),
    path('video', views.video, name='video'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)