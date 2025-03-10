from django.contrib import admin

from ..models import *


class RamBuildInline(admin.TabularInline):
    """
    Inline admin class for RAM in PC build
    editing.
    """
    model = RamBuild
    extra = 0
    fields = ('quantity', 'ram')


class StorageBuildInline(admin.TabularInline):
    """
    Inline admin class for storage in PC build
    editing.
    """
    model = StorageBuild
    extra = 0
    fields = ('quantity', 'storage')


class PcBuildAdmin(admin.ModelAdmin):
    """
    Admin class for PC build display and editing,
    uses inlines to edit RAM and storage in that build.
    """
    list_display = ('title', 'cpu_disp', 'gpu_disp', 'ram_disp', 'storage_disp')
    list_filter = ('gpu__brand', 'cpu__brand', 'gpu__gpu_model', 'cpu__cpu_model')
    search_fields = ('title', 'gpu__brand', 'gpu__gpu_model', 'cpu__brand', 'cpu__cpu_model')

    inlines = (RamBuildInline, StorageBuildInline)


class RamBuildAdmin(admin.ModelAdmin):
    """
    Admin class for RamBuild display, it is used in PC build.
    """
    list_display = ('ram_title', 'ram_capacity', 'ram_speed', 'quantity', 'pc_build_name')
    list_filter = ('ram__ram_type',)
    search_fields = ('ram__ram_name', 'ram__ram_type')


class StorageBuildAdmin(admin.ModelAdmin):
    """
    Admin class for StorageBuild display, it is used in PC build.
    """
    list_display = ('storage_title', 'storage_capacity', 'storage_write_speed', 'storage_read_speed')
    list_filter = ('storage__storage_type',)
    search_fields = ('storage__storage_type', 'storage__storage_name')


class PcBuildListingAdmin(admin.ModelAdmin):
    """
    Admin class for PC build listings to be
    displayed, edited, filtered.
    """
    list_display = ('pc_name', 'date_created', 'condition', 'main_specs', 'price', 'display_seller', 'listing_seller')
    list_editable = ('condition', 'price', 'listing_seller')
    list_filter = ('condition', 'pc_build__cpu__brand', 'pc_build__gpu__brand')
    search_fields = ('pc_build__title', 'pc_build__gpu__brand', 'pc_build__gpu__gpu_model',
                     'pc_build__cpu__brand', 'pc_build__cpu__cpu_model')


class UserLikesAdmin(admin.ModelAdmin):
    """
    This admin class is for user likes,
    easier display, easier to read.
    """
    list_display = ('user', 'pcbuild_listing')


# PC build
admin.site.register(PcBuild, PcBuildAdmin)
admin.site.register(RamBuild, RamBuildAdmin)
admin.site.register(StorageBuild, StorageBuildAdmin)
admin.site.register(PcBuildListing, PcBuildListingAdmin)
admin.site.register(UserLikes, UserLikesAdmin)
