from django.contrib import admin

# Register your models here.
from starshop import models

admin.site.register(models.Star)
admin.site.register(models.Author)
admin.site.register(models.Quote)

