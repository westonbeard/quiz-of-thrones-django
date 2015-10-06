from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import RequestContext, loader

from quiz.models import Question, Answer
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'quiz/index.html'


    def get_queryset(self):
        return Question.objects.all()
