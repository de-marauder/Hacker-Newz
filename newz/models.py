from datetime import datetime
from django.db import models

# Create your models here.


class LatestNewsModel (models.Model):

    id = models.IntegerField(primary_key=True)
    post_data = models.JSONField()
    pub_date = models.IntegerField()
    custom_post = models.BooleanField()

    def __str__(self):
        return f'Hacker news {self.id}'
