from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortKey = request.GET["sort"]
            sort = sortKey
            if sortKey == "name":
                sortKey == "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortKey = f"-{sortKey}"
            products = products.order_by(sortKey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "search" in request.GET:
            query = request.GET["search"]
            if not query:
                messages.error(request, "You didn't enter anything to search.")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """
    A view to show a specific product.
    """

    product = get_object_or_404(Product, pk=product_id)
    # Update to be products only in same section
    # related_products = Product.objects.all()
    related_products = Product.objects.filter(category=product.category).exclude(
        sku=product.sku
    )

    context = {"product": product, "related_products": related_products}

    return render(request, "products/product_detail.html", context)
