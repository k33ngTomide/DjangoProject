from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

import user
from user.models import TweeterUser


# Register your models here.

@admin.register(TweeterUser)
class UserAdmin(BaseUserAdmin):
    pass

    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             "classes": ("wide",),
    #             "fields": ("username", "password1", "password2", 'first_name', 'lastname', 'email'),
    #         },
    #     ),
    # ),