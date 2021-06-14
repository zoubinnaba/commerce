from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from auctions.models import (
    User,
    Listing,
    Bid, Comment,
)
from auctions.forms import ListingModelForm, CommentModelForm


def index(request):
    listings = Listing.objects.filter(available=True).order_by('-created')
    context = {
        "listings": listings
    }
    return render(request, "auctions/index.html", context)


def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    bid_price = Bid.objects.all()
    comments = Comment.objects.all().filter(listing=listing)
    context = {
        'listing': listing,
        'bid_price': bid_price,
        'comments': comments
        # 'offer': offer
    }
    if request.method == 'POST':
        form = CommentModelForm(request.POST or None)
        if form.is_valid():
            body = request.POST["body"]
            form = Comment.objects.create(
                listing=listing,
                body=body
            )
            form.save()
            # offer = Bid.make_bid()
            context = {
                'form': form,
                'listing': listing,
                'comments': comments
            }
            return render(request, "auctions/listing_detail.html", context)
    form = CommentModelForm()
    context['form'] = form
    return render(request, "auctions/listing_detail.html", context)


def listing_create(request):
    form = ListingModelForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            # img_obj = form.instance
            form.save()
            return redirect('index')
        else:
            form = ListingModelForm()
    return render(request, "auctions/listing_create.html", {'form': form})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
