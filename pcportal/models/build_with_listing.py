from datetime import date
from .seller_model import *
from .part_models import *
from django.contrib.auth.models import User


class PcBuild(models.Model):
    """
    PcBuild model stores information about Pc builds.
    title - the name of Pc,
    cpu, cpu cooler, gpu, psu, motherboard, pc case,
    all these parts are accessed through a foreign key to each.
    ram and storage parts through related_name, then they are gathered
    if they are multiple and returned as f strings.
    """
    title = models.CharField("PC name", max_length=50, blank=True, null=True)
    cpu = models.ForeignKey(Cpu, on_delete=models.SET_NULL, blank=True, null=True)
    cpucooler = models.ForeignKey(CpuCooler, on_delete=models.SET_NULL, blank=True, null=True)
    gpu = models.ForeignKey(Gpu, on_delete=models.SET_NULL, blank=True, null=True)
    psu = models.ForeignKey(Psu, on_delete=models.SET_NULL, blank=True, null=True)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.SET_NULL, blank=True, null=True)
    pc_case = models.ForeignKey(CasePC, on_delete=models.SET_NULL, blank=True, null=True)

    def title_disp(self):
        """
        This function displays pc build's title
        if there isn't one, returns Untitled.
        """
        if self.title:
            return f"{self.title}"
        else:
            return "Untitled"

    title_disp.short_description = "PC name"

    def cpu_disp(self):
        """
        This function displays cpu brand and model.
        """
        if self.cpu:
            return f"{self.cpu.brand} {self.cpu.cpu_model}"
        else:
            return "No Cpu"

    cpu_disp.short_description = "CPU"

    def cooler_disp(self):
        """
        This function displays a cpu cooler.
        """
        if self.cpucooler:
            return f"{self.cpucooler.cooler_name}"
        else:
            return "No CPU cooler"

    cooler_disp.short_description = "CPU COOLER"

    def gpu_disp(self):
        """
        This function displays a gpu model.
        """
        if self.gpu:
            return f"{self.gpu.gpu_model}"
        else:
            return "No GPU"

    gpu_disp.short_description = "GPU"

    def psu_disp(self):
        """
        This function displays a PSU.
        """
        if self.psu:
            return f"{self.psu.psu_name}"
        else:
            return "No PSU"

    psu_disp.short_description = "PSU"

    def motherboard_disp(self):
        """
        This function displays a Motherboard.
        """
        if self.motherboard:
            return f"{self.motherboard.motherboard_name}"
        else:
            return "No motherboard"

    motherboard_disp.short_description = "MOTHERBOARD"

    def casepc_disp(self):
        """
        This function displays a PC case.
        """
        if self.pc_case:
            return f"{self.pc_case.case_name}"
        else:
            return "No pc case"

    casepc_disp.short_description = "PC CASE"

    def ram_disp(self):
        """
        This functions uses related_name (ram) and
        then joins ram quantity and capacity into f strings
        and returns them.
        """
        # noinspection PyUnresolvedReferences
        if self.ram.exists():
            ram_detes = []
            # noinspection PyUnresolvedReferences
            for ram_build in self.ram.all():
                ram_detes.append(f"{ram_build.quantity}x{ram_build.ram.capacity}GB")
            rams = ', '.join(ram_detes)
            return f"{rams} RAM"
        else:
            return "No RAMs"

    ram_disp.short_description = "RAM"

    def storage_disp(self):
        """
        This functions uses related_name (storage) and
        then joins storage quantity, capacity, type
        into f strings and returns them.
        """
        # noinspection PyUnresolvedReferences
        if self.storage.exists():
            storages_detes = []
            # noinspection PyUnresolvedReferences
            for storage_build in self.storage.all():
                storages_detes.append(f"{storage_build.quantity}x{storage_build.storage.capacity}GB "
                                      f"{storage_build.storage.storage_type}")
            storages = ', '.join(storages_detes)
            return f"{storages}"
        else:
            return "No storage"

    storage_disp.short_description = "Storage"

    def __str__(self):
        return f"{self.cpu_disp()} {self.gpu_disp()}, {self.ram_disp()}, {self.storage_disp()}"


# RAM quantity and Storage quantity for PC BUILD

class RamBuild(models.Model):
    """
    This class uses a foreign key to link RAM
    to a specific pc build while also setting quantity of
    RAM sticks
    """
    quantity = models.IntegerField("RAM quantity",
                                   help_text="Quantity of RAMs")
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    pcbuild = models.ForeignKey(PcBuild, on_delete=models.CASCADE, related_name="ram")

    def ram_title(self):
        """
        returns ram name and type.
        """
        return f"{self.ram.ram_name} {self.ram.ram_type}"

    def ram_capacity(self):
        """
        returns ram capacity in GB,
        calls ram_display() through ram foreign key.
        """
        return f"{self.ram.ram_display()}"

    def ram_speed(self):
        """
        returns ram speed in GHz,
        calls speed_display() through ram foreign key.
        """
        return f"{self.ram.speed_display()}"

    def pc_build_name(self):
        """
        returns pc build's title
        calls title_disp() through pcbuild foreign key.
        """
        return f"{self.pcbuild.title_disp()}"

    def __str__(self):
        return (f"{self.ram.ram_name}, {self.quantity}x{self.ram.capacity}, "
                f"{self.ram.ram_type}, {self.ram.ram_speed}, {self.pcbuild.title}")

    class Meta:
        verbose_name = "RAM stick for a build"
        verbose_name_plural = "RAM sticks for a build"


class StorageBuild(models.Model):
    """
    This class uses a foreign key to link storage devices
    to a specific pc build while also setting quantity of
    storage devices
    """
    quantity = models.IntegerField("Storage quantity",
                                   help_text="Quantity of Storage devices")
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    pcbuild = models.ForeignKey(PcBuild, on_delete=models.CASCADE, related_name="storage")

    def storage_title(self):
        """
        returns storage's title.
        """
        return f"{self.storage.storage_name}"

    def storage_capacity(self):
        """
        returns storage's type and capacity in GB.
        """
        return f"{self.storage.storage_type} {self.storage.capacity_display()}"

    def storage_write_speed(self):
        """
        returns storage's write speed.
        """
        return f"{self.storage.write_display()}"

    def storage_read_speed(self):
        """
        returns storage's read speed.
        """
        return f"{self.storage.read_display()}"

    def __str__(self):
        return (f"{self.storage.storage_name}, {self.storage.storage_type}, "
                f"{self.quantity}x{self.storage.capacity}GB")

    class Meta:
        verbose_name = "Storage device for a build"
        verbose_name_plural = "Storage devices for a build"


# PC build listing model

class PcBuildListing(models.Model):
    """
    This class links pc build to a seller,
    allowing to set price for a pc build,
    condition and description.
    """
    price = models.FloatField("Price")
    date_created = models.DateField("Date listed", auto_now_add=True)

    expiration_date = models.DateField("Expiration date", default="2100-01-01")

    PC_CONDITION = (
        ("full", "Full build"),
        ("incomplete", "Incomplete"),
        ("pre-owned", "Pre-owned"),
    )
    condition = models.CharField("PC condition", choices=PC_CONDITION,
                                 help_text="Is is a full build, incomplete or used",
                                 max_length=30)

    description = models.TextField("Description",
                                   max_length=500, blank=True, null=True,
                                   help_text="PC build description, information")
    pc_build = models.ForeignKey(PcBuild, on_delete=models.CASCADE, related_name="pcbuildlisting")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="pcbuildlisting")

    listing_seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def exp_status(self):
        if self.expiration_date < date.today():
            return "Expired"
        return "Active"

    def pc_name(self):
        """
        This function returns PC build's brand and model.
        """
        return f"{self.pc_build.title}"

    def main_specs(self):
        """
        This function returns PC build's main specifications.
        """
        return f"{self.pc_build.gpu_disp()}, {self.pc_build.cpu_disp()}, {self.pc_build.ram_disp()}"

    def display_seller(self):
        return f"{self.seller.f_name} {self.seller.l_name}"

    display_seller.short_description = "SELLER"

    def __str__(self):
        return (f"{self.pc_name()} {self.date_created}. price - {self.price}, "
                f"condition - {self.condition}, seller - {self.seller}")
