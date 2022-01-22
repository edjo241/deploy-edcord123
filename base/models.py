from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User




# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=CASCADE,null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    #participants=
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering=['-updated','-created']
    
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    room=models.ForeignKey(Room,on_delete=CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

