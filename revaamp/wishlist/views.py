from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_saved(request):
    """
    A view that renders the wishlist page
    """
    return render(request, "wishlist/saved_ads.html")


def add_to_saved(request, item_id):
    """
    Add a product to the saved ads section
    """
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get("redirect_url")
    saved = request.session.get("saved", {})

    if item_id in list(saved.keys()):
        messages.info(request, f"You have already saved this item")
    else:
        saved[item_id] = item_id
        messages.success(request, f"Added {product.name} to your wishlist.")

    request.session["saved"] = saved
    return redirect(redirect_url)


def remove_from_saved(request, item_id):
    """
    Remove an item from the wishlist
    """
    product = get_object_or_404(Product, pk=item_id)
    try:
        saved = request.session.get("saved", {})
        saved.pop(item_id)
        messages.success(request, f"Removed {product.name} from wishlist")
        request.session["saved"] = saved
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Oops! Something went wrong. {e}")
        return HttpResponse(status=500)
