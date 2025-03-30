from django.urls import path

from tasks.apps import TasksConfig
from tasks.views import (
    TaskCreateAPIView,
    TaskDestroyAPIView,
    TaskUpdateAPIView,
)

app_name = TasksConfig.name

urlpatterns = [
    path("create/", TaskCreateAPIView.as_view(), name="create"),
    path("<int:pk>/update/", TaskUpdateAPIView.as_view(), name="update"),
    path("<int:pk>/destroy/", TaskDestroyAPIView.as_view(), name="destroy"),
]