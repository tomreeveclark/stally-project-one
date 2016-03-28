from django.contrib import admin
from .models import UserProfile, Market, Stall, Application, Booking, Event

# Register your models here.

class MarketAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    #exclude = ('slug',)

admin.site.register(Market, MarketAdmin)
admin.site.register(UserProfile)
admin.site.register(Stall)
admin.site.register(Application)
admin.site.register(Booking)
admin.site.register(Event)
# Register your models here.

