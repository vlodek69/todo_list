from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
