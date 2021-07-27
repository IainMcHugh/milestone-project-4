from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from comments.models import Comment
from products.models import Product
from profiles.models import UserProfile
from .forms import CommentForm


def view_comments(request, product_id):
    """
    A view that renders the comments page for a product
    """
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product)
    form = CommentForm()

    context = {
        "product_id": product_id,
        "comments": comments,
        "form": form,
        "max_rating": 5,
    }

    return render(request, "comments/comments.html", context)


def add_comment(request, product_id):
    """
    Add a comment for a product
    """
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = get_object_or_404(Product, pk=product_id)
            comment.user = UserProfile.objects.get(user=request.user)
            comment.save()
            messages.success(request, "Successfully added a coment.")
            return redirect(reverse("product_detail", args=[product_id]))
        else:
            messages.error(
                request, "Failed to add comment. Please ensure the form is valid."
            )

    return render(request, "home/index.html")
