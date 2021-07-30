from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

# Context processor
def cart_contents(request):
    """
    A context processor that will make cart contents available throughout the entire application
    """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get("cart", {})

    for item_id, quantity in cart.items():
        try:
            product = Product.objects.filter(soft_delete=False).get(pk=item_id)
            total += quantity * product.price
            product_count += quantity
            cart_items.append(
                {"item_id": item_id, "quantity": quantity, "product": product}
            )
        except Product.DoesNotExist:
            continue

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    if cart.items():
        first_item_id = list(cart.items())[0][0]
        first_product = get_object_or_404(Product, pk=first_item_id)

    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
