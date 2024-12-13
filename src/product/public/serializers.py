from rest_framework import serializers

from src.product.models import Product, ProductCategory, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "slug", "description"]


class PublicProductListSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "business",
            "category",
            "name",
            "description",
            "price",
            "offer_price",
            "stock_quantity",
            "unit",
            "images",
        ]
