from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from . import models

# Create your views here.


class AllReviewsList(ListView):
    model = models.Review
    template_name = "reviews/list.html"
    context_object_name = "reviews"


class ReviewView(CreateView):
    model = models.Review
    template_name = "reviews/review.html"
    fields = '__all__'

    def get_success_url(self):
        return reverse("thank-you")


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"


class ReviewDetail(DetailView):
    model = models.Review
    template_name = "reviews/detail.html"
