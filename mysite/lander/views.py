from datetime import datetime
from django.db.models.fields import DateTimeField
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import AddAnswer, AskQuestionForm, CommentForm, RegisterForm
from lander.models import Answer, Comments, Question,User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    questions = Question.objects.all()
    return render(request,'lander/index.html',{'questions': questions})
    
def ask_question(request):
    context={}

    form = AskQuestionForm(request.POST or None)

    if form.is_valid():
        final = form.save(commit=False)
        final.user = User.objects.get(id = request.user.id)
        final.save()

    context['form'] = form
    return render(request, "lander/ask_question.html", context)

def question_detail(request,question_heading):

    context = {}
    question = Question.objects.get(question_heading = question_heading)
    answers = Answer.objects.filter(question__question_heading = question_heading)

    comments = Comments.objects.filter(question__question_heading = question_heading)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        final = form.save(commit=False)
        final.user = User.objects.get(id = request.user.id)
        final.question = Question.objects.get(question_heading = question_heading)
        # final.post_date = datetime.now()
        final.save()

    context = {'form':form, 'comments':comments, 'question':question,'answers':answers}
    return render(request, 'lander/question_detail.html',context)

def add_answer(request,question_heading):
    context = {}
    form = AddAnswer(request.POST or None)

    if form.is_valid():
        final = form.save(commit=False)
        final.user = User.objects.get(id = request.user.id)
        final.question = Question.objects.get(question_heading = question_heading)
        final.save()
        messages.success(request,'Answered successfully')

    context = {'form': form}
    return render(request, "lander/add_answer.html", context)

def register(response):
    form = RegisterForm(response.POST)
    if form.is_valid():
        form.save()
        
        return redirect("/")

    context = {'form':form}
    return render(response,"lander/register.html", context)

