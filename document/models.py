from django.db import models


# Возможные приоритеты хранятся в Базе Данных
class Priority(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)


class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.RESTRICT,
                                 db_column='priority')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
