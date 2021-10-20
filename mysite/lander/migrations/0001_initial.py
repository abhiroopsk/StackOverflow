# Generated by Django 3.0.6 on 2021-10-14 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans_text', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('upvote', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_heading', models.CharField(max_length=20, null=True)),
                ('question_text', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UpvoteQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lander.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvote_question', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UpvoteAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lander.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upvote_answer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DownvoteQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lander.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downvote_question', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DownvoteAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lander.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downvote_answer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lander.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lander.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lander.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
