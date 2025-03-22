from django.db import models

class Point(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.JSONField()  # {"latitude": 12.34, "longitude": 56.78}
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Polygon(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.JSONField()  # GeoJSON format
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
