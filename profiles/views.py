from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

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
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        image = request.FILES["image"]
        print(image)
        print(type(image))
        save_jpg_image(image)
        return redirect("profiles:upload")
