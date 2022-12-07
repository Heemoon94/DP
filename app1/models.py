from django.db import models

# Create your models here.


class Nobel(models.Model) :
    sTitle = models.CharField(max_length=250)
    sIndex = models.CharField(max_length=100)
    sAbstract = models.CharField(max_length=250)
    tPublish = models.DateTimeField()

    def __str__(self) -> str :
        return super().__str__()