from django.contrib import admin
from todo.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
  list_display = ("title", 'status')

admin.site.register(Task, TaskAdmin)