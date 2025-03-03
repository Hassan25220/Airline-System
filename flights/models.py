from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") # models.CASCADE is lya use kr rha hai k bad ma kabhi humne airport delete kerna pare tu hum kr sake gy.
    # origin = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
    
