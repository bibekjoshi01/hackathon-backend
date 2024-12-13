from django.db import models

from src.base.models import AbstractInfoModel
from src.user.models import User


class BusinessCategory(AbstractInfoModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BusinessInfo(AbstractInfoModel):
    farmer = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name="business_info"
    )
    category = models.ForeignKey(BusinessCategory, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    business_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    story = models.TextField(blank=True)
    contact_email = models.EmailField()
    contact_no = models.CharField(max_length=15)

    def __str__(self):
        return self.business_name
