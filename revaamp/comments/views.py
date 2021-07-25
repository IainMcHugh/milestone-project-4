from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from comments.models import Comment
from profiles.models import UserProfile
from .forms import CommentForm


def view_comments(request, product_id):
    """
    A view that renders the comments page for a product
    """

    comments = Comment.objects.filter(product=product_id)
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
        print(form)
        if form.is_valid():
            test = form.save(commit=False)
            test.user = UserProfile.objects.get(user=request.user)
            test.save()
            messages.success(request, "Successfully added a coment.")
            return redirect(reverse("product_detail", args=[product_id]))
        else:
            messages.error(
                request, "Failed to add comment. Please ensure the form is valid."
            )

    return render(request, "home/index.html")


# def remove_comment(request, item_id):
#     """
#     Remove a comment from a product
#     """
#     product = get_object_or_404(Product, pk=item_id)
#     try:
#         saved = request.session.get("saved", {})
#         saved.pop(item_id)
#         messages.success(request, f"Removed {product.name} from wishlist")
#         request.session["saved"] = saved
#         return HttpResponse(status=200)
#     except Exception as e:
#         messages.error(request, f"Oops! Something went wrong. {e}")
#         return HttpResponse(status=500)
