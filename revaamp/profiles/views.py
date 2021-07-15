from django.shortcuts import get_object_or_404, render

from .models import UserProfile


def profile(request):
    """
    Display the users profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        "profile": profile
    }
    return render(request, template, context)
