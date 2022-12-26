from django.contrib import admin

from .models import PostModel

admin.site.register(PostModel)
# Must register each model to Admin for it to be accessible in admin.

# Register your models here.
