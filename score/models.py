from django.db import models


class Scores(models.Model):
    by = models.CharField(max_length=30)
    predict = models.IntegerField()

