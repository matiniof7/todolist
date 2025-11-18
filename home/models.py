from django.db import models


class Todos(models.Model):
    title=models.CharField()
    details=models.CharField()
    create=models.TimeField()
    owner=models.IntegerField()
    

