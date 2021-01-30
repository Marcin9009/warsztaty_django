from django.urls import path

from . import views


app_name = 'romm_reservation'

urlpatterns = [
    path('', views.RoomView, name='room')
]