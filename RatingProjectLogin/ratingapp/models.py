from django.db import models
from django import forms


class Sentence(models.Model):
    sno = models.IntegerField(unique=True)
    source = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    class Meta:
        ordering = ('sno',)

    def __str__(self):
        return f"Sentence {self.sno}"


class SentenceForm(forms.ModelForm):
    class Meta:
        model = Sentence
        fields = ['source', 'target']