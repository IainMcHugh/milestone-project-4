from django.db import models

from products.models import Product
from profiles.models import UserProfile


class SavedProduct(models.Model):
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="wishlist",
    )

    def __str__(self):
        return self.product.name
