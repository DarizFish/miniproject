from django.db import models

# Create your models here.
class Message(models.Model):
    user_name = models.CharField(max_length=20)
    message_text = models.CharField(max_length=200)
    create_date = models.DateTimeField()