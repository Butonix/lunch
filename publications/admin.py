from django.contrib import admin
from . import models

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    ModelAdmin class that
    is going to control how we display the Article object
    on the admin
    """
    pass


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    ModelAdmin class that
    is going to control how we display the Category object
    on the admin
    """
    pass


@admin.register(models.Magazine)
class MagazineAdmin(admin.ModelAdmin):
    """
    ModelAdmin class that
    is going to control how we display the Magazine object
    on the admin
    """
    pass
