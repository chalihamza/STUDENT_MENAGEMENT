from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class UserModel(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser, UserModel)
