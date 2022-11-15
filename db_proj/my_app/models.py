from django.db import models

# Create your models here.
class employe(models.Model):
    id = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=40)
    e_des = models.CharField(max_length=20)
    e_sal = models.IntegerField(default=100)

