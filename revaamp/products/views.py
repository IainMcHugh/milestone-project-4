from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """

    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """
    A view to show a specific product.
    """

    product = get_object_or_404(Product, pk=product_id)
    # Update to be products only in same section
    related_products = Product.objects.all()

    context = {"product": product, "related_products": related_products}

    return render(request, "products/product_detail.html", context)
