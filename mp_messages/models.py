from django.db import models


class Message(models.Model):
    date = models.DateTimeField()
    message_text = models.TextField()
    image_url = models.CharField(max_length=255, primary_key=True)
    tag = models.CharField(max_length=255)
