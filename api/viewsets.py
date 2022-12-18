from rest_framework import viewsets
from . import models
from . import serializers

class ProfileViewset(viewsets.ModelViewSet):
    queryset =  models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

# this viewset automatically make some functions which are:
# create()
# retrieve() => only retrive one data
# list() => same as retrive but retrieve multiple data
# update()
# destroy()