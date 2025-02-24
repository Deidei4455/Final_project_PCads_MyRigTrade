from django.contrib import admin

from ..models import *


class CpuAdmin(admin.ModelAdmin):
    list_display = ('brand', 'cpu_model', 'cores', 'speed_display', 'socket_type')
    list_filter = ('brand',)
    search_fields = ('brand', 'cpu_model', 'socket_type')


class GpuAdmin(admin.ModelAdmin):
    list_display = ('brand', 'gpu_model', 'vram_display', 'speed_display')
    list_filter = ('brand',)
    search_fields = ('brand', 'gpu_model', 'vram')


class PsuAdmin(admin.ModelAdmin):
    list_display = ('psu_name', 'wattage', 'efficiency')
    list_filter = ('efficiency',)
    search_fields = ('psu_name', 'wattage', 'efficiency')


class RamAdmin(admin.ModelAdmin):
    list_display = ('ram_name', 'ram_display', 'ram_type', 'speed_display')
    list_filter = ('ram_type',)
    search_fields = ('ram_name', 'ram_type', 'ram_speed')


class StorageAdmin(admin.ModelAdmin):
    list_display = ('storage_name', 'storage_type', 'capacity_display', 'write_display', 'read_display')
    list_filter = ('storage_type',)
    search_fields = ('storage_name', 'storage_type', 'capacity')


class CasePCAdmin(admin.ModelAdmin):
    list_display = ('case_name', 'case_size')
    list_filter = ('case_size',)
    search_fields = ('case_name', 'case_size')


class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('motherboard_name', 'chipset', 'socket_type', 'ram_type', 'board_size', 'ram_display')
    list_filter = ('chipset', 'socket_type', 'ram_type', 'board_size')
    search_fields = ('motherboard_name', 'chipset', 'socket_type', 'ram_type', 'board_size')


class CpuCoolerAdmin(admin.ModelAdmin):
    list_display = ('cooler_name', 'cooler_type', 'max_power', 'fan_size_display')
    list_filter = ('cooler_type',)
    search_fields = ('cooler_name', 'cooler_typet', 'max_power', 'fan_size')


# PC parts
admin.site.register(Cpu, CpuAdmin)
admin.site.register(Gpu, GpuAdmin)
admin.site.register(Psu, PsuAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(CasePC, CasePCAdmin)
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(CpuCooler, CpuCoolerAdmin)
