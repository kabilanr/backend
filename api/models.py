from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.name
