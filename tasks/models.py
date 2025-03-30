from django.db import models

NULLABLE = {"blank": True, "null": True}


class Performer(models.Model):
    """Модель исполнителя"""

    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        help_text="Введите имя",
    )

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    def __str__(self):
        return self.name


class Task(models.Model):
    """Модель задачи"""

    data_create = models.DateTimeField(
        auto_now_add=True,
        **NULLABLE,
        verbose_name="Время создания",
    )

    performer = models.ForeignKey(
        Performer,
        on_delete=models.CASCADE,
        verbose_name="Исполнитель",
    )

    PRIORITY_FIRST = 1
    PRIORITY_SECOND = 2
    PRIORITY_THIRD = 3
    PRIORITY = [
        (PRIORITY_FIRST, "Высокий приоритет"),
        (PRIORITY_SECOND, "средний приоритет"),
        (PRIORITY_SECOND, "низкий приоритет"),
    ]
    priority = models.IntegerField(
        choices=PRIORITY,
        verbose_name="Уровень приоритетности",
        default=0,
    )

    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )

    comments = models.CharField(
        max_length=1000,
        verbose_name="Комметарии",
        help_text="Введите комметарии",
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
