from django.shortcuts import get_object_or_404
from products.models import Product

# Context processor
def saved_contents(request):
    print("Saved Contents Processor")
    saved_items = []
    product_count = 0
    related_products_wishlist = None
    saved = request.session.get("saved", {})

    for item_key, item_value in saved.items():
        product = get_object_or_404(Product, pk=item_value)
        print(product)
        print("***")
        product_count += product_count
        saved_items.append({"item_id": item_value, "product": product})

    if saved.items():
        first_item_id = list(saved.items())[0][0]
        first_product = get_object_or_404(Product, pk=first_item_id)

        related_products_wishlist = Product.objects.filter(
            category=first_product.category
        ).exclude(sku=first_product.sku)

    context = {
        "saved_items": saved_items,
        "product_count": product_count,
        "related_products_wishlist": related_products_wishlist,
    }

    return context
