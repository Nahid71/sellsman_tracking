from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location, MackAddress, Assign

@admin.register(Location)
class ShopAdmin(OSMGeoAdmin):
    list_display = ( 'location', 'address' )

@admin.register(MackAddress)
class ShopAdmin(OSMGeoAdmin):
    list_display = ( 'employee', 'address' )

@admin.register(Assign)
class ShopAdmin(OSMGeoAdmin):
    list_display = ( 'employee', 'date', 'area', 'status' )