from api.viewsets import *
from  rest_framework import routers

router = routers.DefaultRouter()
router.register('profile',ProfileViewset)
router.register('Wallet',WalletViewset)
router.register('Total_History',Total_HistoryViewset)
router.register('Newcard',NewcardViewset)
router.register('Library',LibraryViewset)
router.register('Cart',CartViewset)
router.register('Store',StoreViewset)
router.register('Bus',BusViewset)
router.register('Fee_type',Fee_typeViewset)
router.register('Paylater',PaylaterViewset)
router.register('Settings',SettingsViewset)
router.register('Others',OthersViewset)
router.register('Igoal',IgoalViewset)

