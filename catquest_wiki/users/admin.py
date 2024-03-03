from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as UA
from .models import Users

# Register your models here.

# admin.site.register(Users)
@admin.register(Users)
class UserAdmin(UA):
    fieldsets = (
        (_("Personal info"), {"fields": ("username", "email", "strikes")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_admin",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username", "email", "date_joined", "strikes", "is_active", "is_staff", "is_admin")
    readonly_fields = ('last_login', 'date_joined', 'username')
