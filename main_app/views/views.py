from django.shortcuts import render

from rest_framework import viewsets

from main_app.models.models import (
    Laboratories
)

from main_app.serializers.serializers import (
    LaboratoriesSerializer
)

# Create your views here.
class LaboratoriesViewSet(viewsets.ModelViewSet):
    queryset = Laboratories.objects.all()
    serializer_class = LaboratoriesSerializer
    filterset_fields = (
        'id', 
        'name',
    )
    search_fields = (
        'name',
    )
    my_tags = ["Laboratories"]