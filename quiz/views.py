from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, request
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
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ScoresView, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.all()
        return context

    @property
    def get_score(request):
        num_questions = 3
        correct = 0
        selected_answer_id = Question.objects.all().answer_set.get(pk=request.POST['answer.pk'])
        print selected_answer_id
        # return 0 if not request.POST['answer.pk']
        for question_id,answer_pk in request.POST['answer.pk']:
            setting_question = Question.objects.get(question_id)
            correct_answer_id = setting_question.answer_set.filter(correct=True).first().pk
            if correct_answer_id == int(selected_answer_id):
                correct += 1
            return correct/num_questions
