from rest_framework import serializers

from .models import Product
from src.base.serializers import AbstractInfoRetrieveSerializer


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "offer_price"]


class ProductRetrieveSerializer(AbstractInfoRetrieveSerializer):
    class Meta(AbstractInfoRetrieveSerializer.Meta):
        model = Product
        fields = ["id", "name", "price", "offer_price"]

        fields += AbstractInfoRetrieveSerializer.Meta.fields


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "offer_price"]

    def create(self, validated_data):
        return super().create(validated_data)


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "offer_price"]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)