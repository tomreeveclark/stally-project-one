from django.contrib import admin
from .models import Market, Stall, UserProfile

# Register your models here.
admin.site.register(Market)
#admin.site.register(MarketAdmin)
admin.site.register(Stall)
admin.site.register(UserProfile)

"""
class MarketAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name')}
""" 