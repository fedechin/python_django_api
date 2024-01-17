from django.db import models
import uuid

# Create your models here.

class Joke(models.Model):
    categories = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    icon_url = models.URLField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField()
    value = models.TextField()

    def __str__(self):
        return self.value