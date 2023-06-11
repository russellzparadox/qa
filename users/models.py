from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    body = models.CharField(max_length=3000)
    like = models.ManyToManyField(User, related_name='question')
    who = models.ManyToManyField(Candidate)

    def __str__(self) -> str:
        return self.body

    def tootal_likes(self):
        return self.like.count()
