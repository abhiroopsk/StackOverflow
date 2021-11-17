from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.

class Question(models.Model):
    QUESTION_TAGS = (
        ('WebDev','WebDev'),
        ('Software','Software'),
        ('Django','Django'),
        ('java','java'),
        ('python','python'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_heading = models.CharField(max_length=50, null=True)
    question_text = models.CharField(max_length=1000, null=False)
    post_date = models.DateTimeField(auto_now_add=True)
    ans_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    upvote_count = models.IntegerField(default=0, null=True)
    tags = MultiSelectField(choices = QUESTION_TAGS)

    def __str__(self):
        return self.question_heading

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ans_text = models.CharField(max_length=1000)
    post_date = models.DateTimeField(auto_now_add=True)
    upvote_count = models.IntegerField(default=0, null=True)


class CommentQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)

class CommentAnswer(models.Model):
    answer = models.ForeignKey(Answer,related_name='answer',on_delete=models.CASCADE)
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

class tag_question(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    tag_text = models.CharField(max_length=1, null=True)
