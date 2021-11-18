from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.contrib.auth.models import User
import datetime


from .models import Answer, CommentQuestion,CommentAnswer, Question, tag_question

class AskQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ("question_heading","question_text","tags")

        widgets ={
            'question_heading' : forms.Textarea(attrs={'class':'form-control','maxlength':100,'rows':2}),
            'question_text': forms.Textarea(attrs={'class':'form-control'}),
        }

class AddAnswer(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ("ans_text",)

        widgets ={
            'ans_text': forms.Textarea(attrs={'class':'form-control', 'maxlength':400})
        }

class AddTagForm(forms.ModelForm):

    class Meta:
        model = tag_question
        fields = ("tag_text",)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", 'password1', "password2"]

class CommentQuestionForm(forms.ModelForm):
    class Meta:
        model = CommentQuestion
        fields = ("comment_text",)

        

class CommentAnswerForm(forms.ModelForm):
    class Meta:
        model = CommentAnswer
        fields = ("comment_text",)

        widgets ={
            'comment_text': forms.Textarea(attrs={'class':'form-control', 'rows':1, 'maxlength':50})
        }