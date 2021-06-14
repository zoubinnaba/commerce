from django.urls import path

from auctions.views import (
    listing_detail,
    login_view,
    logout_view,
    index,
    register, listing_create
)

urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>/", listing_detail, name="listing_detail"),
    path("listing_create/", listing_create, name="listing_create"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("register", register, name="register")
]
