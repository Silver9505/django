
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from webapp.views import JuegoViewset,ModalidadViewset,IdiomaViewset,GeneroViewset
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from webapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
]

urlpatterns += staticfiles_urlpatterns()