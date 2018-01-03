from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    """
    ModelAdmin class that
    is going to control how we display the User object
    on the admin
    """
    pass
