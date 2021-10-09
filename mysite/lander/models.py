from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_heading = models.CharField(max_length=20, null=True)
    question_text = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.question_heading

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ans_text = models.CharField(max_length=100)

