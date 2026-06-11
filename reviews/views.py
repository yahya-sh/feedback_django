from django.shortcuts import render, redirect
from . import forms
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from . import models

# Create your views here.


class AllReviewsList(ListView):
    model = models.Review
    template_name = "reviews/list.html"
    context_object_name = "reviews"


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


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"


class ReviewDetail(DetailView):
    model = models.Review
    template_name = "reviews/detail.html"
