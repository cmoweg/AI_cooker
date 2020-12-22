from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FoodImage(models.Model):
    # user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    photo = models.ImageField(upload_to="images/")
    imageIdx = models.SmallIntegerField()
    uploaded = models.DateTimeField(auto_now_add=True)
