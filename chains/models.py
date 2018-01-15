from django.db import models

# Create your models here.


class Story(models.Model):
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    publisher = models.CharField(max_length=200, null=True)
    event_code = models.IntegerField(default=0)
    country = models.CharField(max_length=200, null=True)


class Clause(models.Model):
    id = models.AutoField(primary_key=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    # save clauses as json to save rows
    clauses = models.TextField(default='[]')


class Sentence(models.Model):
    id = models.AutoField(primary_key=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    # save clauses as json to save rows
    sentences = models.TextField(default='[]')


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    # sentence = models.ForeignKey(Clause, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    questions = models.TextField(default='[]')
    # a_text = models.CharField(max_length=200)


class Chain(models.Model):
    id = models.AutoField(primary_key=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=True)
    # store chains as string
    chains = models.TextField(default='[]')
