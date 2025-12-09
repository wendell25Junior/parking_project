from django.contrib import admin
from .models import Floor, Sector, ParkingSpot

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "floor")
    list_filter = ("floor",)


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "sector", "get_floor", "is_occupied")
    list_filter = ("sector", "sector__floor", "is_occupied")
    search_fields = ("code",)

    def get_floor(self, obj):
        return obj.sector.floor.name
    
    get_floor.short_description = "Andar"
