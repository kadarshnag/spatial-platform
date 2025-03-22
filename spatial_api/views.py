from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Point, Polygon
from .serializers import PointSerializer, PolygonSerializer


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer
