from django.shortcuts import render, redirect
from . import forms
from django.views import View
from . import models

# Create your views here.
# def review(request):
#     form = forms.ReviewForm(request.POST if request.method == "POST" else None)
#     if request.method == "POST":
#         if form.is_valid():
#             # review = models.Review(**form.cleaned_data)
#             # review.save()
#             form.save()
#             return redirect("thank-you")
#     return render(
#         request,
#         "reviews/review.html",
#         {
#             "form": form,
#         },
#     )

class ReviewView(View):
    def get(self, request):
        form = forms.ReviewForm()
        return render(
            request,
            "reviews/review.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thank-you")

        return render(
            request,
            "reviews/review.html",
            {
                "form": form,
            },
        )


def thank_you(request):
    return render(request, "reviews/thank_you.html")
