
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Ardas_Interior_App import API_Views
router = DefaultRouter()

router.register('Product', API_Views.ProductViewSet,basename="Product")


urlpatterns = [
     path('api/',include(router.urls)),
   
    # path('',include('Ardas_Interior_App.urls'))
]
