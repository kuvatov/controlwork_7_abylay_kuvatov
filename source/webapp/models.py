from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    ACTIVE = 'active', 'Активно'
    BLOCKED = 'blocked', 'Заблокировано'


# Create your models here.
class GuestBook(models.Model):
    author = models.CharField(max_length=20, null=False, blank=False, verbose_name="Имя автора")
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False, verbose_name="Email")
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    edited_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время изменения")
    status = models.CharField(max_length=20, null=False, blank=False, choices=StatusChoice.choices,
                              default=StatusChoice.ACTIVE, verbose_name="Статус")

    def __str__(self):
        return f'{self.author} | {self.email} | {self.status}'

    def delete(self, using=None, keep_parents=False):
        self.status = StatusChoice.BLOCKED
        self.save()

    class Meta:
        verbose_name_plural = 'Guest Book'
