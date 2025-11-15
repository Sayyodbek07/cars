from django.db import models


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_year = models.IntegerField(max_length=100)
    car_color = models.CharField(max_length=100)
    car_speed = models.IntegerField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.car_year} {self.car_name}"