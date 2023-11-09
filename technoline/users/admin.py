from django.contrib import admin

from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile_picture', 'user', 'phone', 'address')


admin.site.register(Profile, ProfileAdmin)
