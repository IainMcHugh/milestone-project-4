from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """

    products = Product.objects.filter(soft_delete=False).all()
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
            if sortKey == "category":
                sortKey == "category__name"
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

    related_products = Product.objects.filter(category=product.category).exclude(
        sku=product.sku, soft_delete=True
    )

    context = {"product": product, "related_products": related_products}

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, "Permission denied")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added a product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    form = ProductForm()
    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store.
    """
    if not request.user.is_superuser:
        messages.error(request, "Permission denied")
        return redirect(reverse("home"))

    product = Product.objects.filter(soft_delete=False).get(pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store.
    """
    if not request.user.is_superuser:
        messages.error(request, "Permission denied")
        return redirect(reverse("home"))

    product = Product.objects.filter(soft_delete=False).get(pk=product_id)
    product.soft_delete = True
    product.save()

    messages.success(request, "Product deleted")
    return redirect(reverse("products"))


@login_required
def add_comment(request):
    """
    Add a comment for a product
    """
    messages.success(request, "Comment added")
    return redirect(reverse("products"))
