from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from wishlist.models import SavedProduct
from profiles.models import UserProfile
from products.models import Product


def view_saved(request):
    """
    A view that renders the wishlist page
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    saved = SavedProduct.objects.filter(user=profile)
    context = {"saved_items": saved}
    return render(request, "wishlist/saved_ads.html", context)


def add_to_saved(request, item_id):
    """
    Add a product to the saved ads section
    """
    redirect_url = request.POST.get("redirect_url")

    product = get_object_or_404(Product, pk=item_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    currently_saved = SavedProduct.objects.filter(user=profile, product=product)
    if currently_saved:
        messages.info(request, f"You have already saved this item")
    else:
        saved = SavedProduct(product=product, user=profile)
        saved.save()
        messages.success(request, f"Added {product.name} to your wishlist.")

    return redirect(redirect_url)


def remove_from_saved(request, item_id):
    """
    Remove an item from the wishlist
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        saved = SavedProduct.objects.filter(product=product)
        saved.delete()
        messages.success(request, f"Removed {product.name} from wishlist")
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Oops! Something went wrong. {e}")
        return HttpResponse(status=500)
