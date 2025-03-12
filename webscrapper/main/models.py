from django.db import models
from django.utils import timezone
class PageModel(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    posted_at = models.TimeField(default=timezone.now().date())
