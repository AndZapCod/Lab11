from django.db import models


class Scores(models.Model):
    score = models.IntegerField()
    origin = models.CharField(max_length=30)
    date = models.DateField()

