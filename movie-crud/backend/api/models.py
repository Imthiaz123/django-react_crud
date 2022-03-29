from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=50)
    starring = models.CharField(max_length=300)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
