from django.urls import path
from . import views
from .views import (index, ask_question, question_detail,add_answer, update_answer,upvote_answer,upvote_question,user_profile,update_question
,update_answer,add_tag,comment_answer,search_question)
urlpatterns = [
    path('', views.index, name='index'),
    path('ask-question', views.ask_question, name='ask_question'),
    # path('add_tag/<question_id>', views.add_tag, name='add_tag'),
    path('update_question/<int:question_id>', views.update_question, name='update_question'),
    path('update_answer/<int:question_id>/<int:answer_id>', views.update_answer, name='update_answer'),
    path('comment_answer/<int:question_id>/<int:answer_id>', views.comment_answer, name='comment_answer'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('register', views.register, name='register'),
    path('add-answer/<int:question_id>', views.add_answer, name='add_answer'),
    path('question/<int:question_id>', views.question_detail, name='question_detail'),
    path('<int:question_id>/<int:answer_id>/upvote_answer', views.upvote_answer, name='upvote_answer'),
    path('<int:question_id>/upvote_question', views.upvote_question, name='upvote_question'),
    path('search_question', views.search_question, name='search_question'),

]