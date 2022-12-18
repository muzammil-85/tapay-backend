# serializer are used manage the api , 
# which means that sending python queries in the form of json request to  external app or something


from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Profile
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
