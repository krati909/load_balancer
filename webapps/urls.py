# webapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/hello/', views.hello_view, name='hello'),
    path('worker/stats/', views.stats_view, name='stats')]