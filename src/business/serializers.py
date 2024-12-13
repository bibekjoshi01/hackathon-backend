from rest_framework import serializers
from .models import BusinessDocuments, BusinessInfo, BusinessCategory


class BusinessCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCategory
        fields = ["id", "name"]


class BusinessInfoSerializer(serializers.ModelSerializer):
    is_verified = serializers.SerializerMethodField()

    class Meta:
        model = BusinessInfo
        fields = [
            "category",
            "latitude",
            "longitude",
            "logo",
            "business_name",
            "description",
            "story",
            "contact_email",
            "contact_no",
            "is_verified",
        ]

    def get_is_verified(self, obj):
        return obj.documents.is_verified


class BusinessInfoRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    is_verified = serializers.SerializerMethodField()

    class Meta:
        model = BusinessInfo
        fields = [
            "category",
            "latitude",
            "longitude",
            "logo",
            "business_name",
            "description",
            "story",
            "contact_email",
            "contact_no",
            "is_verified",
        ]

    def get_is_verified(self, obj):
        return obj.documents.is_verified


class BusinessDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDocuments
        fields = [
            "registration_certificate",
            "tax_certificate",
            "owner_id",
            "address_proof",
        ]
