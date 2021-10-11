from django.contrib import admin
from .models import Comments, Question, Answer
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comments)