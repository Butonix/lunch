from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home Page
    # See article by slug
    # See magazines by slug
    # Search articles and magazines by tags
    # Create account
    # Log in
    # See user profile
    # Edit user profile
    # See reading list
    # Write article
    # Edit article
    # See categories list
]

admin.site.site_header = "Lunch Admin"
