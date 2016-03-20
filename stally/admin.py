from django.contrib import admin
from .models import Market, Stall, UserProfile, Event

# Register your models here.
admin.site.register(Market)
#admin.site.register(MarketAdmin)
admin.site.register(Stall)
admin.site.register(UserProfile)
admin.site.register(Event)

"""
class MarketAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name')}


class EventAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		obj.name = form.market.name
		obj.location = form.market.location
"""