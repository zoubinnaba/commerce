from django.contrib import admin
from auctions.models import User, Listing, Category, Bid

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Bid)
