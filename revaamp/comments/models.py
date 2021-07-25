from django.db import models
from products.models import Product
from profiles.models import UserProfile

# Create your models here.


class Comment(models.Model):
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE, default=""
    )
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="comment",
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=False, blank=False, default=0)
    comment = models.CharField(max_length=256, null=False, blank=False, default="")
