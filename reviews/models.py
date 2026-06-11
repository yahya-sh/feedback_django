from django.db import models
from django.core import validators
from django.urls import reverse


# Create your models here.
class Review(models.Model):
    username = models.CharField(
        max_length=255,
        validators=[
            validators.MinLengthValidator(3),
        ],
    )
    feedback = models.TextField()
    rating = models.IntegerField(
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(5),
        ]
    )

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.username} (Rate {self.rating} of 5)"
