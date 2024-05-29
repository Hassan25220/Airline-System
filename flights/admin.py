from django.contrib import admin

from .models import Airport, Flights, Passenger

# Register your models here.
# if we want to see some more information in django admin

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


# If we want to update Passenger admin
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)



admin.site.register(Airport)
admin.site.register(Flights, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)