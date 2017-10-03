from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    userId = models.IntegerField(default=1)
    title = models.CharField(default="Default Title", max_length = 190)
    body = models.TextField(default='Body of post goes here')
    # registration_date = models.DateField(default=datetime.date.today())
    # graduation_date = models.DateField(default = datetime.date.today)
