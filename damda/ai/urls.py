from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings


app_name = "ai"
urlpatterns = [
    path('', views.index, name='index'),
    path('name-form/', views.name_form, name='name-form'),
    path('name-result/', views.name_result, name='name-result'),
    path('face/', views.face, name='face' ),
    path('video', views.video, name='video'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)