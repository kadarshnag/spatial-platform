from django.contrib import admin
from .models import Point, Polygon

@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'coordinates', 'created_at')

@admin.register(Polygon)
class PolygonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'coordinates', 'created_at')
