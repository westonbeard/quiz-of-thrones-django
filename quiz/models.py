from django.db import models


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
