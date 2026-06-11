from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView
from . import models

# Create your views here.


class AllReviewsList(ListView):
    model = models.Review
    template_name = "reviews/list.html"
    context_object_name = "reviews"


class ReviewView(FormView):
    form_class = forms.ReviewForm
    template_name = "reviews/review.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("thank-you")


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"


class ReviewDetail(DetailView):
    model = models.Review
    template_name = "reviews/detail.html"
