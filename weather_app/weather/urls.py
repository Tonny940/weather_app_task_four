from django.urls import path

from weather_app.weather import views

urlpatterns = (
    path('', views.index),
)
