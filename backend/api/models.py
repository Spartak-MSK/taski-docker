"""Database models for tasks."""

from django.db import models


class Task(models.Model):
    """Task model representing a to-do item."""

    title = models.CharField(verbose_name="Заголовок", max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Return a human-readable representation of the task."""
        return self.title
