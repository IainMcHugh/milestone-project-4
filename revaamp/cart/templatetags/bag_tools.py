from django import template

register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    """
    Simple template tag to return total price for entire quantity of specific cart item.
    """
    return price * quantity
