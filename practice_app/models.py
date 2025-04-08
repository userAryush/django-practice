from django.db import models
from django.utils import timezone
# Create your models here.

class AppVariety(models.Model):
    APP_TYPE_CHOICE = [
        ('pubg','game'),
        ('spotify','music'),
        ('netflix','video'),
        ('uber','ride'),
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='practices/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=10, choices= APP_TYPE_CHOICE)
    
    def __str__(self):
        return self.name   # yesle garda admin panel ma naya data create garda name aauxa instead or obj1, obj2
    