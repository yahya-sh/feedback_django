from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from . import forms
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


class CreateProfileView(View):
    def get(self, request):
        form = forms.UserProfileForm()
        return render(
            request,
            "profiles/create_profile.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = forms.UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = models.UserProfile(**form.cleaned_data)
            profile.save()
            return redirect("profiles:upload")
        return render(
            request,
            "profiles/create_profile.html",
            {
                "form": form,
            },
        )
