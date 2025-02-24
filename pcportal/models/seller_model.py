from django.db import models
from django.contrib.auth.models import User


class Seller(models.Model):
    """
    This model stores information about the seller,
    first name, last name, email and phone number.
    """
    f_name = models.CharField("First name", max_length=30)
    l_name = models.CharField("Last name", max_length=30)
    email = models.CharField("Email", max_length=30)
    phone_num = models.IntegerField("Phone number")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')

    @property
    def count_all_listings(self):
        # noinspection PyUnresolvedReferences
        return (self.pcbuildlisting.count() + self.cpu_listing.count() + self.gpu_listing.count() +
                self.psu_listing.count() + self.ram_listing.count() + self.storage_listing.count() +
                self.casepc_listing.count() + self.motherboard_listing.count() +
                self.cpucooler_listing.count())

    def full_name(self):
        return f"{self.f_name} {self.l_name}"

    full_name.short_description = "FULL NAME"

    def __str__(self):
        return f"{self.f_name} {self.l_name}, {self.email}, {self.phone_num}"


class SellerReview(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Review content', max_length=2000)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True)

    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.date_created}, {self.reviewer}, {self.seller}, {self.content[:50]}"
