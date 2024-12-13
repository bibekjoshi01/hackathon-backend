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
    category_name = serializers.CharField(source="category.name")
    average_rating = serializers.SerializerMethodField() 
    total_reviews = serializers.SerializerMethodField() 

    class Meta:
        model = Product
        fields = [
            "id",
            "business",
            "category_name",
            "name",
            "description",
            "price",
            "offer_price",
            "stock_quantity",
            "unit",
            "featured_image",
            "average_rating",
            "total_reviews"
        ]

    def get_average_rating(self, obj):
        return obj.average_rating()
    
    def get_total_reviews(self, obj):
        return obj.total_reviews()
    
