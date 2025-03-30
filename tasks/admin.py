from django.contrib import admin

from tasks.models import Performer, Task


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "data_create", "performer", "priority", "title", "comments")
    list_filter = ("priority",)