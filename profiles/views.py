from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, ListView
from . import models
# Create your views here.


def save_jpg_image(image):
    try:
        with open(f"temp/{image.name}", "wb") as dest:
            for chunk in image.chunks():
                dest.write(chunk)
        return True
    except Exception:
        return False


class CreateUserProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = models.UserProfile
    fields = "__all__"

    def get_success_url(self):
        return reverse("profiles:upload")


class AllUserProfileList(ListView):
    model = models.UserProfile
    template_name = "profiles/profile_list.html"
    context_object_name = "profiles"
