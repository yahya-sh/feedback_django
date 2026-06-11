from django.db import models


# Create your models here.
class UserProfile(models.Model):
    image = models.ImageField(upload_to="user_profile_images")

    def __str__(self):
        return self.image.name
