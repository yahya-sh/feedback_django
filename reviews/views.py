from django.shortcuts import render


# Create your views here.
def render(request):
    return render(request, "reviews/review.html")
