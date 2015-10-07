from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import RequestContext, loader

from quiz.models import Question, Answer
# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'quiz_list'
    template_name = 'quiz/index.html'
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        return context


class ScoresView(TemplateView):
    template_name = 'quiz/scores.html'

