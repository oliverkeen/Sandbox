import datetime
from django.db import models
from django.utils import timezone

# Contains series of classes that Django's ORM converts to database tables
# Create your models here.

class Question(models.Model):
    # Column_Name = Field_Class_Instance()
    question_text = models.CharField(max_length=200) # Requires max_length value
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # Defines relationship, where each Choice is related to a single Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text