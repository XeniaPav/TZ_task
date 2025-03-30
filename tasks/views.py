from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from tasks.serializers import TaskSerializer
from tasks.models import Task
class TaskCreateAPIView(CreateAPIView):
    """CRUD для создания задачи"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskUpdateAPIView(UpdateAPIView):
    """CRUD для изменения задачи"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
class TaskDestroyAPIView(DestroyAPIView):
    """CRUD для удаления задачи"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

