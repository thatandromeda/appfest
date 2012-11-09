from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html') 

def open(request):
    return render(request, 'open.html', {
        'context': context,
    }) 
    
def question(request, question_id):
    return render(request, 'question.html', {
        'context': context,
    }) 