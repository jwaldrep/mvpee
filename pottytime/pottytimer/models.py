from django.db import models

class Sticker(models.Model):
    text = models.TextField(default='0')