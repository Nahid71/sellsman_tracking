from django.contrib.auth import get_user_model
from django.contrib.gis.db import models


User = get_user_model()



STATUS_CHOICES = (
    ('V', 'Visit'),
    ('NV', 'Not Visit')
)

class Location(models.Model):
    location = models.PointField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address
    
class MackAddress(models.Model):
    employee = models.ForeignKey(User,  on_delete=models.CASCADE)
    address  = models.CharField( max_length=52)

    def __str__(self):
        return self.employee.email

class Assign(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date     = models.DateField(auto_now_add=True)
    area     =models.ForeignKey(Location,  on_delete=models.CASCADE)
    status   = models.CharField(choices=STATUS_CHOICES, max_length=2)

    def __str__(self):
        return self.employee.email



