from django.db import models
from django.utils.timezone import now


# Create your models here.
class CarMake(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    def __str__(self):
        return self.Name , self.Description
class CarModel(models.Model):
    CHOICES = (
    ('1', ' Sedan'),
    ('2', 'SUV'),
    ('3', ' WAGON'),
    

)
    carmodel = models.ForeignKey(CarMake,on_delete=models.CASCADE)
    Dealer_id = models.IntegerField()
    Type = models.CharField(max_length=200,choices=CHOICES)
    year =  models.DateField()
    def __str__(self):
        return self.carmodel , self.Type ,self.year


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
