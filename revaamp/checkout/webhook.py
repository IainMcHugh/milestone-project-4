from django.http import Http404
from django.http.response import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe webkooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected wehbook event
        """
        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)
