from api.viewsets import ProfileViewset
from  rest_framework import routers

router = routers.DefaultRouter()
router.register('profile',ProfileViewset)

# url will be like this :
#   localhost:8000/api/employee/
# methods are GET , POST , PUT , DELETE