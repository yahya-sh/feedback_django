from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, View
from . import models
from django.shortcuts import redirect
from django.http.response import Http404
# Create your views here.


def set_faviourite_review_id(request, id):
    request.session["favourite_review_id"] = id


def get_faviourite_review_id(request):
    request.session.get("favourite_review_id")


def is_favourite_review_id(request, id):
    return get_faviourite_review_id(request, id) == str(id)


class AllReviewsList(ListView):
    model = models.Review
    template_name = "reviews/list.html"
    context_object_name = "reviews"


class ReviewView(CreateView):
    model = models.Review
    template_name = "reviews/review.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("thank-you")


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"


class ReviewDetail(DetailView):
    model = models.Review
    template_name = "reviews/detail.html"

    def get_context_data(self, object, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_favourite"] = is_favourite_review_id(self.request, object.pk)
        return context


class FavouriteView(View):
    def post(self, request):
        review_id = request.POST.get("review_id")
        set_faviourite_review_id(request, review_id)

        if not review_id:
            raise Http404()
        return redirect("detail", pk=review_id)
