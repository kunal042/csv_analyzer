from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('process/<int:pk>/', views.process_file, name='process_file'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
