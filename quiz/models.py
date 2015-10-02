from django.db import models


class Question(models.Model):
    content = models.CharField(max_length=300)


class Answer(models.Model):
    content = models.CharField(max_length=300)
    correct = models.BooleanField()
    question_id = models.ForeignKey(Question)
