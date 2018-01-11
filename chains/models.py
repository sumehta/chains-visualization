from django.db import models

# Create your models here.


class Story(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    publisher = models.CharField(max_length=200)
    event_code = models.IntegerField(default=0)
    country = models.CharField(max_length=200)


class Sentence(models.Model):
    id = models.AutoField(primary_key=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    num = models.IntegerField(default=-1)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    q_text = models.CharField(max_length=200)
    a_text = models.CharField(max_length=200)


class Chain(models.Model):
    id = models.AutoField(primary_key=True)
