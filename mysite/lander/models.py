from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_heading = models.CharField(max_length=20, null=True)
    question_text = models.CharField(max_length=100, null=False)
    post_date = models.DateTimeField(auto_now_add=True)
    ans_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    upvote_count = models.IntegerField(default=0, null=True)


    def __str__(self):
        return self.question_heading

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    ans_text = models.CharField(max_length=100, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    upvote_count = models.IntegerField(default=0, null=True)


class CommentQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)

class CommentAnswer(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)

class UpvoteAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    upvotes = models.IntegerField(default=0, null=True)

class DownvoteAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvote_answer')

class UpvoteQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvote_question')
    upvotes = models.IntegerField(default=0, null=True)

class DownvoteQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvote_question')

