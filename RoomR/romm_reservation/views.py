from django.shortcuts import render
from django.utils import timezone
from .models import Romm
from django.views import View

class RoomView(View):
    def get(self, request):
        ctx = {
            'room_name': Romm.objects.get(pk)
        }
        return render(request, "char_data.html", ctx)
