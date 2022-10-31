from django.contrib import admin

from .models import Enquirty


class EnquirtyAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone_number", "message"]


admin.site.register(Enquirty, EnquirtyAdmin)
