
from django.db import models
from djangotoolbox.fields import ListField
# Create your models here.
from djangotoolbox.fields import EmbeddedModelField

class Cameras(models.Model):
    Idcamera= models.CharField()
    Name= models.CharField()
    Planta= models.CharField()
    URL= models.CharField()
    SafetyRegion = models.CharField()

class Images(models.Model):
    Idimage = models.CharField()
    Idcamera = models.CharField()
    acquisition_time = models.CharField()
    update_time = models.CharField()
    Status = models.CharField()
    JsonReturned = models.CharField()
    EztaskReturn = models.CharField()
    RawImage = models.CharField()
    ProcessedImage = models.CharField()
    AnomalyGroup = models.CharField()
    AccuracyCheck = models.CharField()


