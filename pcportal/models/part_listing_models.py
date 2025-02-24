from .part_models import *
from .seller_model import *
from django.contrib.auth.models import User
from datetime import date


class PartListing(models.Model):
    """
    A base model for part listings for
    less duplicate codes.
    Abstract True means a table of this
    model will not be created in database.
    Part listings may inherit this model.
    date_created - date when a part was listed.
    quantity is the amount of parts.
    price is how much a part is on sale for.
    """
    date_created = models.DateField("Date listed", auto_now_add=True)

    expiration_date = models.DateField("Expiration date", default="2025-03-20")

    quantity = models.IntegerField("quantity",
                                   help_text="Quantity of units")
    price = models.FloatField("Price per piece")

    listing_seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def exp_status(self):
        if self.expiration_date < date.today():
            return "Expired"
        return "Active"

    class Meta:
        abstract = True


class CpuListing(PartListing):
    """
    Listing for CPUs
    """
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name="cpu_listing")

    def cpu_name(self):
        """
        This function returns CPU's brand and model.
        """
        return f"{self.cpu.brand} {self.cpu.cpu_model}"

    def display_seller(self):
        return f"{self.seller.f_name} {self.seller.l_name}"

    display_seller.short_description = "SELLER"

    def __str__(self):
        return (f'{self.cpu.brand} {self.cpu.cpu_model}, quantity - {self.quantity},'
                f' price for one - {self.price}')


class GpuListing(PartListing):
    """
    Listing for GPUs
    """
    gpu = models.ForeignKey(Gpu, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name="gpu_listing")

    def gpu_name(self):
        """
        This function returns GPU's brand and model.
        """
        return f"{self.gpu.brand} {self.gpu.gpu_model}"

    def display_seller(self):
        return f"{self.seller.f_name} {self.seller.l_name}"

    display_seller.short_description = "SELLER"

    def __str__(self):
        return (f'{self.gpu.brand} {self.gpu.gpu_model}, quantity - {self.quantity},'
                f' price for one - {self.price}')


class PsuListing(PartListing):
    """
    Listing for PSUs
    """
    psu = models.ForeignKey(Psu, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name="psu_listing")

    def psu_title(self):
        """
        This function returns PSU's name.
        """
        return f"{self.psu.psu_name}"

    def display_seller(self):
        return f"{self.seller.f_name} {self.seller.l_name}"

    display_seller.short_description = "SELLER"

    def __str__(self):
        return (f'{self.psu.psu_name}, quantity - {self.quantity},'
                f' price for one - {self.price}')


class RamListing(PartListing):
    """
    Listing for RAMs
    """
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name="ram_listing")

    def ram_title(self):
        """
        This function returns RAM's name.
        """
        return f"{self.ram.ram_name}"

    def display_seller(self):
        return f"{self.seller.f_name} {self.seller.l_name}"

    display_seller.short_description = "SELLER"

    def __str__(self):
        return (f'{self.ram.ram_name}, quantity - {self.quantity},'
                f' price for one - {self.price}')


class StorageListing(PartListing):
    """
    Listing for storage devices
    """
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name="storage_listing")

    def storage_title(self):
        """
        This function returns Storage's name.
        """
        return f"{self.storage.storage_name}"

    def display_seller(self):
        return f"{self.seller.f_name} {self.seller.l_name}"

    display_seller.short_description = "SELLER"

    def __str__(self):
        return (f'{self.storage.storage_name}, quantity - {self.quantity},'
                f' price for one - {self.price}')


class CasePCListing(PartListing):
    """
    Listing for Pc cases
    """
    casepc = models.ForeignKey(CasePC, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name="casepc_listing")

    def casepc_title(self):
        """
        This function returns PC case's name.
        """
        return f"{self.casepc.case_name}"

    def display_seller(self):
        return f"{self.seller.f_name} {self.seller.l_name}"

    display_seller.short_description = "SELLER"

    def __str__(self):
        return (f'{self.casepc.case_name}, quantity - {self.quantity},'
                f' price for one - {self.price}')

    class Meta:
        verbose_name = "PC case listing"
        verbose_name_plural = 'PC case listings'


class MotherboardListing(PartListing):
    """
    Listings for motherboards
    """
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name="motherboard_listing")

    def motherboard_title(self):
        """
        This function returns motherboard's name.
        """
        return f"{self.motherboard.motherboard_name}"

    def display_seller(self):
        return f"{self.seller.f_name} {self.seller.l_name}"

    display_seller.short_description = "SELLER"

    def __str__(self):
        return (f'{self.motherboard.motherboard_name}, quantity - {self.quantity},'
                f' price for one - {self.price}')


class CpuCoolerListing(PartListing):
    """
    Listing for CPU coolers
    """
    cpucooler = models.ForeignKey(CpuCooler, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name="cpucooler_listing")

    def cooler_title(self):
        """
        This function returns CPU cooler's name.
        """
        return f"{self.cpucooler.cooler_name}"

    def display_seller(self):
        return f"{self.seller.f_name} {self.seller.l_name}"

    display_seller.short_description = "SELLER"

    def __str__(self):
        return (f'{self.cpucooler.cooler_name}, quantity - {self.quantity},'
                f' price for one - {self.price}')
