from django.db import models


class Chat(models.Model):
    room = models.CharField(max_length=255)
    allowed_users = models.IntegerField(default=0)

    def __str__(self):
        return self.room