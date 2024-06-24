from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    list_editable =['completed']
admin.site.register(Todo, TodoAdmin)