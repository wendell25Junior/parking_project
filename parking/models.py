from django.db import models

class Floor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sector(models.Model):
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='sectors')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.floor.name} - {self.name}"


class ParkingSpot(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='spots')
    code = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sector.floor.name} - {self.sector.name} - {self.code}"
