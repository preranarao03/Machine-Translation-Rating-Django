# models.py
from django.db import models
from django.contrib.auth.models import User

class Sentence(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sno = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    class Meta:
        permissions = [
            ("can_add_sentence", "Can add sentences"),
        ]

    def __str__(self):
        return f"Sentence {self.sno}: {self.source} -> {self.target}"
