from django.db import models




class Romm(models.Model):
    '''
        CREATE A MODELS
    '''
    room_name = models.CharField(max_length=255, unique=True)
    room_volume = models.IntegerField(default=0)
    status = models.BooleanField(default=False)


