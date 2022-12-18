from rest_framework import viewsets
from . import models
from . import serializers

class ProfileViewset(viewsets.ModelViewSet):
    queryset =  models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class WalletViewset(viewsets.ModelViewSet):
    queryset =  models.Wallet.objects.all()
    serializer_class = serializers.WalletSerializer
class Total_HistoryViewset(viewsets.ModelViewSet):
    queryset =  models.Total_History.objects.all()
    serializer_class = serializers.Total_HistorySerializer
class NewcardViewset(viewsets.ModelViewSet):
    queryset =  models.Newcard.objects.all()
    serializer_class = serializers.NewcardSerializer
class LibraryViewset(viewsets.ModelViewSet):
    queryset =  models.Library.objects.all()
    serializer_class = serializers.LibrarySerializer
class CartViewset(viewsets.ModelViewSet):
    queryset =  models.Cart.objects.all()
    serializer_class = serializers.CartSerializer
class StoreViewset(viewsets.ModelViewSet):
    queryset =  models.Store.objects.all()
    serializer_class = serializers.StoreSerializer
class BusViewset(viewsets.ModelViewSet):
    queryset =  models.Bus.objects.all()
    serializer_class = serializers.BusSerializer
class Fee_typeViewset(viewsets.ModelViewSet):
    queryset =  models.Fee_type.objects.all()
    serializer_class = serializers.Fee_typeSerializer
class PaylaterViewset(viewsets.ModelViewSet):
    queryset =  models.Paylater.objects.all()
    serializer_class = serializers.PaylaterSerializer
class SettingsViewset(viewsets.ModelViewSet):
    queryset =  models.Settings.objects.all()
    serializer_class = serializers.SettingsSerializer
class OthersViewset(viewsets.ModelViewSet):
    queryset =  models.Others.objects.all()
    serializer_class = serializers.OthersSerializer
class IgoalViewset(viewsets.ModelViewSet):
    queryset =  models.Igoal.objects.all()
    serializer_class = serializers.IgoalSerializer


# this viewset automatically make some functions which are:
# create()
# retrieve() => only retrive one data
# list() => same as retrive but retrieve multiple data
# update()
# destroy()