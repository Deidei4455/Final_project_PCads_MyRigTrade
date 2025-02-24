from django.contrib import admin

from ..models import *


class CpuListingAdmin(admin.ModelAdmin):
    list_display = ('cpu_name', 'date_created', 'quantity', 'price', 'display_seller', 'listing_seller')
    list_editable = ('quantity', 'listing_seller')
    list_filter = ('cpu__brand',)
    search_fields = ('cpu__brand', 'cpu__cpu_model', 'cpu__socket_type', 'seller__f_name', 'seller__l_name')


class GpuListingAdmin(admin.ModelAdmin):
    list_display = ('gpu_name', 'date_created', 'quantity', 'price', 'display_seller', 'listing_seller')
    list_editable = ('quantity', 'listing_seller')
    list_filter = ('gpu__brand',)
    search_fields = ('gpu__brand', 'gpu__gpu_model', 'seller__f_name', 'seller__l_name')


class PsuListingAdmin(admin.ModelAdmin):
    list_display = ('psu_title', 'date_created', 'quantity', 'price', 'display_seller', 'listing_seller')
    list_editable = ('quantity', 'listing_seller')
    list_filter = ('psu__efficiency',)
    search_fields = ('psu__psu_name', 'psu__wattage', 'psu__efficiency')


class RamListingAdmin(admin.ModelAdmin):
    list_display = ('ram_title', 'date_created', 'quantity', 'price', 'display_seller', 'listing_seller')
    list_editable = ('quantity', 'listing_seller')
    list_filter = ('ram__ram_type',)
    search_fields = ('ram__ram_name', 'ram__ram_type', 'ram__capacity')


class StorageListingAdmin(admin.ModelAdmin):
    list_display = ('storage_title', 'date_created', 'quantity', 'price', 'display_seller', 'listing_seller')
    list_editable = ('quantity', 'listing_seller')
    list_filter = ('storage__storage_type',)
    search_fields = ('storage__storage_name', 'storage__storage_type')


class CasePCListingAdmin(admin.ModelAdmin):
    list_display = ('casepc_title', 'date_created', 'quantity', 'price', 'display_seller', 'listing_seller')
    list_editable = ('quantity', 'listing_seller')
    list_filter = ('casepc__case_size',)
    search_fields = ('casepc__case_name', 'casepc__case_siz')


class MotherboardListingAdmin(admin.ModelAdmin):
    list_display = ('motherboard_title', 'date_created', 'quantity', 'price', 'display_seller', 'listing_seller')
    list_editable = ('quantity', 'listing_seller')
    list_filter = ('motherboard__ram_type', 'motherboard__board_size')
    search_fields = ('motherboard__ram_type', 'motherboard__ram_type', 'motherboard__motherboard_name')


class CpuCoolerListingAdmin(admin.ModelAdmin):
    list_display = ('cooler_title', 'date_created', 'quantity', 'price', 'display_seller', 'listing_seller')
    list_editable = ('quantity', 'listing_seller')
    list_filter = ('cpucooler__cooler_type',)
    search_fields = ('cpucooler__cooler_type', 'cpucooler__cooler_name')


# PC part listings
admin.site.register(CpuListing, CpuListingAdmin)
admin.site.register(GpuListing, GpuListingAdmin)
admin.site.register(PsuListing, PsuListingAdmin)
admin.site.register(RamListing, RamListingAdmin)
admin.site.register(StorageListing, StorageListingAdmin)
admin.site.register(CasePCListing, CasePCListingAdmin)
admin.site.register(MotherboardListing, MotherboardListingAdmin)
admin.site.register(CpuCoolerListing, CpuCoolerListingAdmin)
