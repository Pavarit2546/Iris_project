from django.db import models

# Create your models here.
class IrisFlower(models.Model):
    SepalLengthCm = models.FloatField()
    SepalWidthCm = models.FloatField()
    PetalLengthCm = models.FloatField()
    PetalWidthCm = models.FloatField()

    
