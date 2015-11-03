__author__ = 'wbeard'

from django.conf.urls import url
from django.views.generic import TemplateView
from quiz.views import ScoresView

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='quiz_list'),
    url(r'^scores/', ScoresView.as_view(), name='scores'),
]