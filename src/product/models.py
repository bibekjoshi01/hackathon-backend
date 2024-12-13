from django.db import models
from src.base.models import AbstractInfoModel

from src.user.models import User


class ProductCategory(AbstractInfoModel):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "product categories"
        ordering = ["-id"]

    def __str__(self) -> str:
        return self.name


class Product(AbstractInfoModel):
    UNIT_CHOICES = [
        ("kg", "Kilogram"),
        ("piece", "Piece"),
        ("litre", "Litre"),
        ("dozen", "Dozen"),
        ("pack", "Pack"),
    ]

    business = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products"
    )
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, related_name="products"
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default="piece")

    def __str__(self):
        return self.name


# Product Image Model
class ProductImage(AbstractInfoModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return f"Image for {self.product.name}"
