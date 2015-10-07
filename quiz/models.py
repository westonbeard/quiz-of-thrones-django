from django.db import models

from django.db.models import IntegerField


class Question(models.Model):
    content = models.CharField(max_length=300)


    def __str__(self):
        return self.content


class Answer(models.Model):
    content = models.CharField(max_length=300)
    correct = models.BooleanField()
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.content


class User(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.content



class Score(models.Model):
    correct = IntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.content