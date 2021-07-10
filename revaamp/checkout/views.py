from django.shortcuts import redirect, render, reverse

from .forms import OrderForm
from django.contrib import messages

# Create your views here.


def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "There's nothing in your shopping cart")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51JBdtDBfxTbPOaz1CBA6pKp36N2WWIlAsAdc5gBQFigoIYIXF9GMFTTcOPcQoYSBJqZ2TBkLG8zUs1yFBOJQeRej003c0INv8A",
        "client_secret": "revaamp secret",
    }

    return render(request, template, context)
