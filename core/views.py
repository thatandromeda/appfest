from django.shortcuts import render, render_to_response
from appfest.core.models import *
from django.conf import settings

def home(request):
    return render_to_response('askaquestion.html', {'static': settings.STATIC_URL}) 

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
        'context': context,
        'static': settings.STATIC_URL,
    }) 