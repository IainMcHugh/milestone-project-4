from django.db import models
from products.models import Product

# Create your models here.


class SavedProduct(models.Model):
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.product.name
