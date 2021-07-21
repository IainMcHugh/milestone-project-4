from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_saved, name="view_saved"),
    path("add/<item_id>", views.add_to_saved, name="add_to_saved"),
    path("remove/<item_id>", views.remove_from_saved, name="remove_from_saved"),
]
