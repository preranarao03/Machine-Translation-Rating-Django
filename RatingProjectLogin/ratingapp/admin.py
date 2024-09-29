from django.contrib import admin
from .models import Sentence

class SentenceAdmin(admin.ModelAdmin):
    list_display = ['sno','source','target','rating']
admin.site.register(Sentence,SentenceAdmin)
