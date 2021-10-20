from datetime import datetime
from django.db.models.fields import DateTimeField
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import AddAnswer, AskQuestionForm, CommentQuestionForm,CommentAnswerForm, RegisterForm
from lander.models import Answer, CommentQuestion, CommentAnswer, Question, UpvoteAnswer, UpvoteQuestion,User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    questions = Question.objects.all()
    for q in questions:
        answers = Answer.objects.filter(question__pk = q.id)
        count_answers = answers.count()
        question = Question.objects.get(id = q.id)
        comments = CommentQuestion.objects.filter(question__pk = q.id)
        count_comments = comments.count()
        question.ans_count = count_answers
        question.comment_count = count_comments
        question.save()

        

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

def question_detail(request,question_id):

    context = {}
    question = Question.objects.get(pk = question_id)
    question_upvotes = UpvoteQuestion.objects.filter(question__pk = question_id)
    count_question_upvotes=question_upvotes.count()
    question.upvote_count = count_question_upvotes
    question.views +=1
    question.save()
    answers = Answer.objects.filter(question__pk = question_id)
    count_answers = answers.count()

    comments = CommentQuestion.objects.filter(question__pk = question_id).order_by('-post_date')
    count_comments = comments.count()
    form = CommentQuestionForm(request.POST or None)

    if 'comment_question_form' in request.POST:
        if form.is_valid():
            final = form.save(commit=False)
            final.user = User.objects.get(id = request.user.id)
            final.question = Question.objects.get(pk = question_id)
            question.ans_count +=1
            final.save()
            return redirect("/question/"+str(question_id))

    for answer in answers:    
        comment_ans = CommentAnswer.objects.filter(answer__id = answer.id)
        if 'comment_answer_form' in request.POST:
            form = CommentAnswerForm(request.POST or None)
            if form.is_valid():
                final2 = form.save(commit=False)
                final2.user = User.objects.get(id = request.user.id)
                final2.answer = Answer.objects.get(pk = answer.id)
                final2.save()
                return redirect("/question/"+str(question_id))

    #answers
    another_answer = Answer.objects.filter(question__pk = question_id).first()
    for a in answers:
        upvotes = UpvoteAnswer.objects.filter(answer__pk = a.id)
        count_upvotes = upvotes.count()
        another_answer.upvote_count = count_upvotes
        another_answer.save()

    # another_question = Question.objects.filter(pk = question_id)
    # question_upvotes = UpvoteQuestion.objects.filter(question__pk = question_id)
    # count_question_upvotes=question_upvotes.count()

    # # count_question_upvotes = another_question.up.count()
    # another_question.upvote_count = count_question_upvotes
    # another_question.save()


    context = {'question':question,
        'form':form, 'comments':comments, 'answers':answers,
        'count_answers':count_answers, 'count_comments': count_comments,
        # 'comment_ans':comment_ans,
        'count_question_upvotes':count_question_upvotes,
        'count_upvotes':count_upvotes,
        'another_ansewer':another_answer,
        # 'another_question':another_question
    }


    return render(request, 'lander/question_detail.html',context)

def add_answer(request,question_id):
    form = AddAnswer(request.POST or None)

    if form.is_valid():
        final = form.save(commit=False)
        final.user = User.objects.get(id = request.user.id)
        final.question = Question.objects.get(pk = question_id)
        final.save()
        return redirect("/question/"+str(question_id))


    context = {'form': form}
    return render(request, "lander/add_answer.html", context)

def register(response):
    form = RegisterForm(response.POST)
    if form.is_valid():
        form.save()
        
        return redirect("/")

    context = {'form':form}
    return render(response,"lander/register.html", context)


def upvote_answer(request,question_id, answer_id):
    ans = Answer.objects.get(id = answer_id)
    user = request.user
    check = UpvoteAnswer.objects.filter(answer = ans,user=user).count()
    if check >0:
        return redirect("/question/"+str(question_id))
    else:
        UpvoteAnswer.objects.create(
        answer = ans, user = user , upvotes =1)
        return redirect("/question/"+str(question_id))

    # ans.user = user
    # ans.upvotes +=1
    # ans.save()

    
    # ans = Answer.objects.get(id = answer_id)
    # ans.upvotes +=1
    # ans.save()

def upvote_question(request,question_id):
    ques = Question.objects.get(id = question_id)
    user = request.user
    check = UpvoteQuestion.objects.filter(question = ques, user = user).count()
    if check >0:
        return redirect("/question/"+str(question_id))
    else:
        UpvoteQuestion.objects.create(
        question = ques , user = user , upvotes =1)
        return redirect("/question/"+str(question_id))
