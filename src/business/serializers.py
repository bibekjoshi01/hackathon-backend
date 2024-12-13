from rest_framework import serializers
from .models import BusinessInfo, BusinessCategory


class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = ["id", "name"]


class BusinessInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessInfo
        fields = [
            "category",
            "latitude",
            "longitude",
            "business_name",
            "description",
            "story",
            "contact_email",
            "contact_no",
        ]


class BusinessInfoRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")

    class Meta:
        model = BusinessInfo
        fields = [
            "category",
            "latitude",
            "longitude",
            "business_name",
            "description",
            "story",
            "contact_email",
            "contact_no",
        ]
