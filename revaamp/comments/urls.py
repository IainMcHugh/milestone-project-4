from django.urls import path
from . import views

urlpatterns = [
    path("<int:product_id>", views.view_comments, name="view_comments"),
    path("add/<product_id>", views.add_comment, name="add_comment"),
    # path("remove/<product_id>", views.remove_comment, name="remove_comment"),
]
