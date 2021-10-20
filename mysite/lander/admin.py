from django.contrib import admin
from .models import CommentAnswer,CommentQuestion, DownvoteAnswer, Question, Answer, UpvoteAnswer, UpvoteQuestion, DownvoteQuestion
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(CommentQuestion)
admin.site.register(CommentAnswer)
admin.site.register(UpvoteAnswer)
admin.site.register(DownvoteAnswer)
admin.site.register(UpvoteQuestion)
admin.site.register(DownvoteQuestion)