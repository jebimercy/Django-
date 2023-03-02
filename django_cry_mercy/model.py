from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=50, default='Kenya')
    city = models.CharField(max_length=50, default='Nairobi')


def __str__(self):
    return self.name
