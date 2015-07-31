from django.db import models


class Chart(models.Model):
    pass

class Sticker(models.Model):
    text = models.TextField(default='0')
    chart = models.ForeignKey(Chart, default=None)