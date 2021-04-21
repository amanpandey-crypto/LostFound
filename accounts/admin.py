from django.contrib import admin
from .models import ItemData, LostItem, UserProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ItemData)
admin.site.register(LostItem)

