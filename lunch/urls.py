from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home Page
    # See article by slug
    # See magazine by slug
    # Search articles by tags
    # Create account
    # Log in
    # See user profile
    # Edit user profile
    # See reading list
    # Write article
    # Edit article
]

admin.site.site_header = "Lunch Admin"
