from django.shortcuts import render, render_to_response
from appfest.core.models import *
from django.conf import settings
from django import forms
from appfest.core.forms import QuestionForm

def home(request):
    questionform = QuestionForm()
    return render(request, 'askaquestion.html', {
        'static': settings.STATIC_URL, 'questionform': questionform
    }) 

def open(request):
    if Question.objects.count() < 5:
        questions = Question.objects.all()
    else:
        questions = Question.objects.all()[0:5]
    return render(request, 'questionpage.html', {
        'questions': questions,
        'static': settings.STATIC_URL,
    }) 
    
def question(request, question_id):

    return render(request, 'question.html', {
        'static': settings.STATIC_URL,
    }) 