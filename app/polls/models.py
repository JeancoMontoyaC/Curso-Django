from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question=models.CharField(max_length=200)
    pub_date=models.DateTimeField("date published")

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "Preguntas de la Encuesta"

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name_plural = "Opciones de la Encuesta"
    