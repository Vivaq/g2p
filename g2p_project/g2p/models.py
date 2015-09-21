from django.db import models

class Document(models.Model):
    docfile = models.CharField(
        max_length=10000
    )