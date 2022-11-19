from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    esal = models.FloatField()
    email = models.EmailField()

    def __str__(self):
        return f'Name{self.fname} {self.lname}'
    