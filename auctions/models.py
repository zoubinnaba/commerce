from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.title


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=False)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    picture = models.ImageField(upload_to="listings/")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name="comment")
    body = models.TextField(('Comment'), max_length=300)

    def __str__(self):
        return f"{self.listing}"


class Bid(models.Model):
    bid = models.ForeignKey('Listing', related_name="bird_listing", on_delete=models.CASCADE)
    offer = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.offer}"

    def make_bid(self):
        offer_make = self.bid.price + self.offer
        return offer_make