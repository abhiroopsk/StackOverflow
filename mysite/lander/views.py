from datetime import datetime
from django.db.models.fields import DateTimeField
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import AddAnswer, AskQuestionForm, CommentQuestionForm,CommentAnswerForm, RegisterForm, AddTagForm
from lander.models import Answer, CommentQuestion, CommentAnswer, Question, UpvoteAnswer, UpvoteQuestion,User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def search_question(request):
    if request.method == "POST":
        searched = request.POST['searched']
        question_searched = Question.objects.filter(tags__contains = searched)
        return render(request, 'lander/index.html',{'searched':searched,'question_searched':question_searched})
    
    else:
        return render(request, 'lander/index.html')

def index(request):
    questions = Question.objects.all().order_by('-post_date')

    for q in questions:
        answers = Answer.objects.filter(question__pk = q.id)
        question = Question.objects.get(id = q.id)
        comments = CommentQuestion.objects.filter(question__pk = q.id)
        if answers:
            count_answers = answers.count()
            question.ans_count = count_answers
        if comments: 
            count_comments = comments.count()
            question.comment_count = count_comments
        question.save()

        

    return render(request,'lander/index.html',{'questions': questions})
    
def ask_question(request):

    form = AskQuestionForm(request.POST or None)

    if form.is_valid():
        final = form.save(commit=False)
        final.user = User.objects.get(id = request.user.id)
        final.save()

        return redirect('/')
        # form2 = AddTagForm(request.POST or None)
        # if form2.is_valid():
        #     final2 = form2.save(commit=False)
        #     final2.question_id = final.question.id
        #     final2.save()

    context = {
        'form':form, 
        # 'form2':form2
    }
    return render(request, "lander/ask_question.html", context)

def add_tag(request,question_id):
    form = AddTagForm(request.POST or None)
    if form.is_valid():
        final = form.save(commit=False)
        final.question_id = question_id
        final.save()

    context ={
        'form':form 
    }
    return render(request, "lander/add_tag.html",context)

def question_detail(request,question_id):

    context = {}
    question = Question.objects.get(pk = question_id)
    question_upvotes = UpvoteQuestion.objects.filter(question__pk = question_id)
    count_question_upvotes=question_upvotes.count()
    question.upvote_count = count_question_upvotes
    question.views +=1
    question.save()
    answers = Answer.objects.filter(question__pk = question_id).order_by('-upvote_count')
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

    # Comment of answers 
    # comment_ans =[]
    # comments_of_answers =[]
    # for answer in answers:    
    #     comment_ans = CommentAnswer.objects.filter(answer__id = answer.id)
    #     print(comment_ans)
    #     comments_of_answers.append(comment_ans)
    #     print(comments_of_answers)

    #answers
    count_upvotes=''
    another_answer = Answer.objects.filter(question__pk = question_id).first()
    for a in answers:
        upvotes = UpvoteAnswer.objects.filter(answer__pk = a.id)
        if upvotes:
            count_upvotes = upvotes.count()
            a.upvote_count = count_upvotes
            a.save()


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
        # 'comments_of_answers':comments_of_answers,
        # 'another_question':another_question
    }


    return render(request, 'lander/question_detail.html',context)

def comment_answer(request,question_id,answer_id):
    form = CommentAnswerForm(request.POST or None)
    if form.is_valid():
        comment_ans_form_variable = form.save(commit=False)
        comment_ans_form_variable.user = User.objects.get(id = request.user.id)
        comment_ans_form_variable.answer = Answer.objects.get(id = answer_id)
        comment_ans_form_variable.save()
        return redirect("/question/"+str(question_id))
    
    context={'form':form}
    return render(request, 'lander/comment_answer.html',context)
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
        new_user = form.save()
        messages.info(response,"You are now logged in")
        new_user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'],)
        login(response, new_user)
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

def user_profile(request):
    question = Question.objects.filter(user = request.user)
    context = {
        'question':question
    }
    return render(request,"lander/user_profile.html", context)

def update_question(request, question_id):
    question = Question.objects.filter(pk = question_id).first()
    form = AskQuestionForm(request.POST or None, instance=question)

    if form.is_valid():
        form.save()
        return redirect("/question/"+str(question_id))
    context={
        'form':form, 'question':question
    }
    return render(request,"lander/update_question.html", context )


def update_answer(request, question_id,answer_id):
    question = Question.objects.filter(pk = question_id).first()
    answer = Answer.objects.filter(pk = answer_id).first()
    form = AddAnswer(request.POST or None, instance=answer)

    if form.is_valid():
        form.save()
        return redirect("/question/"+str(question_id))
    context={
        'form':form, 'question':question, 'answer':answer
    }
    return render(request,"lander/update_question.html", context )


