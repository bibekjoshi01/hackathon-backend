from rest_framework.generics import ListAPIView

from src.product.models import Product
from src.product.public.serializers import PublicProductListSerializer

class PublicProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = PublicProductListSerializer