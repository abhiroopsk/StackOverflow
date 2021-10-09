from django.urls import path
from . import views
from .views import index, ask_question, question_detail,add_answer

urlpatterns = [
    path('', views.index, name='index'),
    path('ask-question', views.ask_question, name='ask_question'),
    path('register', views.register, name='register'),
    path('add-answer/<question_heading>', views.add_answer, name='add_answer'),
    path('question/<question_heading>', views.question_detail, name='question_detail'),
]