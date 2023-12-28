from django.contrib import admin

from accounts.models import UserProfile, Follower

admin.site.register(UserProfile)
admin.site.register(Follower)