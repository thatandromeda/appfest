from django import forms
from django.db import models
from django.contrib.auth.models import User
from appfest.core.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        widgets = { 
                'user': forms.HiddenInput, 
                'text': forms.Textarea(attrs={'rows' : 4, 'cols' : 75}),
            }