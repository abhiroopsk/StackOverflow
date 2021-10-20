from django.urls import path
from . import views
from .views import index, ask_question, question_detail,add_answer,upvote_answer,upvote_question

urlpatterns = [
    path('', views.index, name='index'),
    path('ask-question', views.ask_question, name='ask_question'),
    path('register', views.register, name='register'),
    path('add-answer/<int:question_id>', views.add_answer, name='add_answer'),
    path('question/<int:question_id>', views.question_detail, name='question_detail'),
    path('<int:question_id>/<int:answer_id>/upvote_answer', views.upvote_answer, name='upvote_answer'),
    path('<int:question_id>/upvote_question', views.upvote_question, name='upvote_question'),
]