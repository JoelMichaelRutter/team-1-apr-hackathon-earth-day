from django.contrib import admin
from .models import ProfileImage

class ProfileImageAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'image',
    )

admin.site.register(ProfileImage, ProfileImageAdmin)
