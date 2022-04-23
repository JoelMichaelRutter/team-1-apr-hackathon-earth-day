from django.contrib import admin
from .models import Recycle, Reduce, Reuse

class RecycleAdmin(admin.ModelAdmin):
    list_display = (
        'action',
        'profile',
        'date',
    )


class ReduceAdmin(admin.ModelAdmin):
    list_display = (
        'action',
        'profile',
        'date',
    )


class ReuseAdmin(admin.ModelAdmin):
    list_display = (
        'action',
        'profile',
        'date',
    )

admin.site.register(Recycle, RecycleAdmin)
admin.site.register(Reduce, ReduceAdmin)
admin.site.register(Reuse, ReuseAdmin)
