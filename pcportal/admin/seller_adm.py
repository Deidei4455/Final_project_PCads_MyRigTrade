from django.contrib import admin

from ..models import *


class SellerAdmin(admin.ModelAdmin):
    """
    Admin class for sellers to be displayed, edited.
    """
    list_display = ('full_name', 'email', 'phone_num', 'user')
    list_editable = ('user',)
    search_fields = ('f_name', 'l_name', 'email', 'phone_num')


# seller
admin.site.register(Seller, SellerAdmin)
