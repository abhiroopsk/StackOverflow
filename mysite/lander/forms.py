from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.contrib.auth.models import User


from .models import Answer, Question

class AskQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ("question_heading","question_text")

class AddAnswer(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ("ans_text",)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", 'password1', "password2"]