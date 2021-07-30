from django import template

register = template.Library()


@register.filter(name="format_date")
def format_date(date):
    """
    Template tag that returns a stripped down timestamp for a comment.
    """
    return date.strftime("%Y/%m/%d")
