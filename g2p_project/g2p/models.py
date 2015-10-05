from django.db import models

class Document(models.Model):
    docfile = models.CharField(
        max_length=10000
    )

class ToSave():
    def __init__(self):
        self.data = ''