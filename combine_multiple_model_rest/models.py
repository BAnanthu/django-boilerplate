from django.db import models


# Create your models here.

class Model1(models.Model):
    model1_item_id = models.AutoField(primary_key=True)
    model1_item_name = models.CharField(max_length=50)


class Model2(models.Model):
    model2_item_id = models.AutoField(primary_key=True)
    model1_item_id = models.ForeignKey(Model1, on_delete=models.CASCADE)
    model2_item_name = models.CharField(max_length=50)
