# serializer are used manage the api , 
# which means that sending python queries in the form of json request to  external app or something


from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Profile
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields

class WalletSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Wallet
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields

class Total_HistorySerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Total_History
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class NewcardSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Newcard
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class LibrarySerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Library
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class CartSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Cart
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class StoreSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Store
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class CanteenSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Canteen
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class BusSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Bus
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class FeesSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Fees
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class Fee_typeSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Fee_type
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class PaylaterSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Paylater
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class SettingsSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Settings
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class ProfileSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Profile
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class OthersSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Others
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
class IgoalSerializer(serializers.ModelSerializer):
    class Meta: # all thing under this class become the object of above class.
        model = Igoal
        fields = '__all__'   # for needed field only ('fullname','mobile'). __all__ is means all the fields
