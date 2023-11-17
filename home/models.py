from django.db import models


class Phone(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
