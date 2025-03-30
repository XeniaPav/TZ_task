from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    """Сериалайзер для задачи"""

    class Meta:
        model = Task
        fields = "__all__"