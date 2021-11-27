from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=300)
    publication_date = models.DateTimeField('published date')

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_desc = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_desc
