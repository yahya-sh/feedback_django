from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def review(request):
    form = forms.ReviewForm(request.POST if request.method == "POST" else None)
    if request.method == "POST":
        if form.is_valid():
            review = models.Review(**form.cleaned_data)
            review.save()
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
