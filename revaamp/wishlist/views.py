from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Prefetch

from wishlist.models import SavedProduct
from profiles.models import UserProfile
from products.models import Product


def view_saved(request):
    """
    A view that renders the wishlist page
    """
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        all_saved = SavedProduct.objects.filter(user=profile)
        saved = all_saved.filter(product__soft_delete=False).prefetch_related(
            Prefetch("product", queryset=Product.objects.filter(soft_delete=False))
        )

        context = {"saved_items": saved}
        return render(request, "wishlist/saved_ads.html", context)
    else:
        messages.info(request, "You need to login first.")
        return redirect(reverse("home"))


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
