from rest_framework.viewsets import ViewSet,ModelViewSet
from Ardas_Interior_App .models import Product
from .serializers import ProductSerliazer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()     
    serializer_class  = ProductSerliazer