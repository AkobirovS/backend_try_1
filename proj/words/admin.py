from django.contrib import admin

from . import models

class WordAdmin(admin.ModelAdmin):
    list_display = ["pk",'word', 'gender']
    list_editable = ["gender",'word']


admin.site.register(models.Words, WordAdmin)