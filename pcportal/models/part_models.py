from django.db import models


class Cpu(models.Model):
    """
    CPU - Central Processing Unit.
    this class - model stores information
    about a specific CPU:
    brand - AMD, Intel..(str),
    cpu_model - e.g. Core i7-12700H..(str),
    cores - number of cores CPU has (int),
    base_clock_speed of CPU in GHz (int),
    socket_type - what socket type cpu is compatible with.
    """
    brand = models.CharField("CPU brand", max_length=30,
                             help_text="CPU brand name")
    cpu_model = models.CharField("CPU model", max_length=30)
    cores = models.IntegerField("Number of cores",
                                help_text="Number of cpu cores",
                                null=True, blank=True)
    base_clock_speed = models.FloatField("Base clock speed",
                                         help_text="Base clock speed of CPU, GHz",
                                         null=True, blank=True)
    socket_type = models.CharField("CPU socket",
                                   max_length=30,
                                   help_text="CPU socket type, (AM4, LGA 1151, etc.)")

    def speed_display(self):
        """
        This function adds GHz next to
        base clock speed. returns speed with GHz
        in an f string.
        """
        return f"{self.base_clock_speed}GHz"

    speed_display.short_description = "BASE CLOCK SPEED"

    def __str__(self):
        return (f"{self.brand} {self.cpu_model}, {self.cores} cores, "
                f"base clock speed - {self.base_clock_speed}GHz, "
                f"socket type - {self.socket_type}")


class Gpu(models.Model):
    """
    GPU - Graphics Processing Unit.
    Gpu class stores information about
    a specific GPU:
    brand - AMD, NVIDIA..(str),
    gpu_model - e.g. Radeon RX 7900 XTX..(str),
    vram is the amount of virtual ram gpu has (int),
    clock_speed is the bas clock speed of GPU in MHz (int).
    """
    brand = models.CharField("GPU brand", max_length=30,
                             help_text="GPU brand name")
    gpu_model = models.CharField("GPU model", max_length=30,
                                 help_text="GPU model (like radeon 7900 xtx, rtx 3090, etc.")
    vram = models.IntegerField("Number of ram")
    clock_speed = models.IntegerField("Base clock speed",
                                      help_text="Clock speed of GPU, MHz",
                                      null=True, blank=True)

    def vram_display(self):
        """
        This function adds GB next to the
        number of vram. returns vram with GB
        in an f string.
        """
        return f"{self.vram}GB"

    vram_display.short_description = "VRAM"

    def speed_display(self):
        """
        This function adds MHz next to clock speed.
        returns clock speed with MHz in an f string.
        """
        return f"{self.clock_speed}MHz"

    speed_display.short_description = "CLOCK SPEED"

    def __str__(self):
        return f"{self.brand} {self.gpu_model} {self.vram}GB, {self.clock_speed}MHz"


class Psu(models.Model):
    """
    PSU - Power Supply Unit.
    This model stores information about
    a specific PSU.
    psu_name - brand, name of PSU, e.g. Corsair TX750 (str),
    wattage is the power output of PSU in watts - W (int),
    efficiency is PSU's efficiency rating, the most common
    one - 80 PLUS Bronze. User gets to choose from given
    efficiency ratings (str).
    """
    psu_name = models.CharField('PSU name', max_length=50)
    wattage = models.IntegerField("PSU wattage power")

    EFF_RATING = (
        ('plus', '80 PLUS'),
        ('bronze', '80 PLUS Bronze'),
        ('silver', '80 PLUS Silver'),
        ('gold', '80 PLUS Gold'),
        ('plat', '80 PLUS Platinum'),
        ('titan', '80 PLUS Titanium'),
    )

    efficiency = models.CharField("PSU efficiency",
                                  choices=EFF_RATING,
                                  default='bronze',
                                  help_text="PSU efficiency rating",
                                  max_length=30)

    def __str__(self):
        return f"{self.psu_name}, {self.wattage}W, {self.efficiency}"


class Ram(models.Model):
    """
    RAM - Random Access Memory.
    Ram model stores information about
    specific RAM modules.
    ram_name is the title of RAM
    e.g. G.Skill Trident Z RGB (str),
    capacity is the amount of RAM that
    module has (int),
    ram_type is the generation of DDR (str),
    ram_speed is RAM module's operating (int)
    speed in MHz (int).
    """
    ram_name = models.CharField("RAM name/title", max_length=50,
                                help_text="RAM name(like G.Skill Trident, Kingston Fury, etc.")
    capacity = models.IntegerField("RAM capacity",
                                   help_text="RAM capacity in GB")
    RAM_TYPE = (
        ('ddr', 'DDR'),
        ('ddr2', 'DDR2'),
        ('ddr3', 'DDR3'),
        ('ddr4', 'DDR4'),
        ('ddr5', 'DDR5'),
    )
    ram_type = models.CharField("RAM type", choices=RAM_TYPE,
                                default='ddr4', max_length=30)
    ram_speed = models.IntegerField("RAM speed", help_text="RAM speed, MHz")

    def ram_display(self):
        """
        This function adds GB next to the
        number of ram. returns ram with GB
        in an f string.
        """
        return f"{self.capacity}GB"

    ram_display.short_description = "CAPACITY"

    def speed_display(self):
        """
        This function adds MHz next to ram speed.
        returns ram speed with MHz in an f string.
        """
        return f"{self.ram_speed}MHz"

    speed_display.short_description = "RAM SPEED"

    def __str__(self):
        return f"{self.ram_name}, {self.capacity}GB, {self.ram_type}, {self.ram_speed}MHz"


class Storage(models.Model):
    """
    Storage - Storage device.
    This model stores information about
    specific storage devices.
    storage_name - name of the storage device e.g. Toshiba X300 (str),
    storage_type - what type of storage is the device (HDD, SSD..) (str),
    capacity is the amount of space in GB storage device has (int),
    write_speed - writing speed of the device in MB/s (int),
    read_speed - reading speed of the device in MB/s (int),
    """
    storage_name = models.CharField("Storage device name", max_length=30,
                                    help_text="Storage device name, Samsung, Kingston, etc.")
    STORAGE_TYPE = (
        ('HDD', 'HDD'),
        ('SSD', 'SSD'),
        ('SSHD', 'SSHD'),
        ('NVMe', 'NVMe'),
        ('M2', 'M.2 - form factor for SSDs'),
    )
    storage_type = models.CharField("Storage type",
                                    choices=STORAGE_TYPE, default='HDD',
                                    max_length=30)
    capacity = models.IntegerField("Storage capacity",
                                   help_text="Storage capacity in GB")
    write_speed = models.IntegerField("Write speed",
                                      help_text="Write speed MB/s")
    read_speed = models.IntegerField("Read speed",
                                     help_text="Read speed MB/s")

    def capacity_display(self):
        """
        This function adds GB next to capacity.
        returns capacity with GB in an f string.
        """
        return f"{self.capacity}GB"

    capacity_display.short_description = "CAPACITY"

    def write_display(self):
        """
        This function adds MB/s next to write speed.
        returns write speed with MB/s in an f string.
        """
        return f"{self.write_speed}MB/s"

    write_display.short_description = "WRITE SPEED"

    def read_display(self):
        """
        This function adds MB/s next to read speed.
        returns read speed with MB/s in an f string.
        """
        return f"{self.read_speed}MB/s"

    read_display.short_description = "READ SPEED"

    def __str__(self):
        return (f"{self.storage_name}, {self.storage_type}, {self.capacity}, "
                f"{self.write_speed}MB/s - write speed, {self.read_speed}MB/s - read speed")


class CasePC(models.Model):
    """
    CasePC - A case for computer parts to store.
    This class stores information about
    specific cases.
    case_name - case brand, name e.g. Cooler Master NR200 (str),
    case_size - case size like full tower, micro-ATK case..(str).
    """
    case_name = models.CharField("Case name", max_length=50,
                                 help_text="PC case name")
    CASE_SIZE = (
        ('full', 'Full Tower'),
        ('mid', 'Mid Tower'),
        ('mini', 'Mini Tower'),
        ('micro-ATX', 'Micro-ATX Case'),
        ('mini-ITX', 'Mini-ITX Case'),
    )
    case_size = models.CharField("Case size", choices=CASE_SIZE, default='mid',
                                 help_text="PC case size, full, mid, mini, micro-ATX, mini-ITX",
                                 max_length=30)

    def __str__(self):
        return f"{self.case_name}, {self.case_size}"

    class Meta:
        verbose_name = "PC case"
        verbose_name_plural = 'PC cases'


class Motherboard(models.Model):
    """
    Motherboard - main printed circuit board (PCB).
    This model stores information about motherboards.
    motherboard_name - e.g. ASUS ROG Strix Z390-I (str),
    chipset - chipset type of the motherboard, e.g. Intel Z390 (str),
    socket_type - what CPU socket type that
    motherboard supports (AM4, LGA 1151..(str)),
    ram_type - what DDR type of ram motherboard supports(str),
    board_size - what size is the motherboard (ATX, Micro ATX..(str)),
    max_ram - maximum capaciry of RAM that motherboard supports (int).
    """
    motherboard_name = models.CharField("Motherboard name", max_length=50,
                                        help_text="Motherboard name, Gigabyte AORUS, ASUS ROG, etc.")
    chipset = models.CharField("Chipset type", max_length=30,
                               help_text="Chipset type, AMD X570, Intel Z790, etc.")
    socket_type = models.CharField("Socket type", max_length=30,
                                   help_text="CPU socket type, (AM4, LGA 1151, etc.)")
    RAM_TYPE = (
        ('ddr', 'DDR'),
        ('ddr2', 'DDR2'),
        ('ddr3', 'DDR3'),
        ('ddr4', 'DDR4'),
        ('ddr5', 'DDR5'),
    )
    ram_type = models.CharField("RAM type", choices=RAM_TYPE,
                                default='ddr4', max_length=30)
    BOARD_SIZE = (
        ('ATX', 'ATX'),
        ('micro ATX', 'Micro ATX'),
        ('mini ATX', 'Mini ATX'),
        ('mini ITX', 'Mini ITX'),
        ('E-ATX', 'E-ATX'),
        ('XL-ATX', 'XL-ATX'),
        ('BTX', 'BTX'),
    )
    board_size = models.CharField(
        "Mootherboard size", choices=BOARD_SIZE, default='micro ATX', max_length=30,
        help_text="Motherboard size, ATX, micro/mini ATX, mini-ITX, E-ATX, XL-ATX, BTX"
    )
    max_ram = models.IntegerField("Max RAM",
                                  help_text="Max RAM capacity that motherboard can have")

    def ram_display(self):
        """
        This function adds GB next to the
        number of ram. returns ram with GB
        in an f string.
        """
        return f"{self.max_ram}GB"

    ram_display.short_description = "MAX RAM"

    def __str__(self):
        return (f"{self.motherboard_name}, {self.chipset}, "
                f"{self.socket_type}, {self.board_size}, {self.max_ram} max RAM, {self.ram_type}")


class CpuCooler(models.Model):
    """
    Cpu cooler to cool the CPU.
    cooler_name - name, brand of cpu cooler - NZXT Kraken Z73.. (str),
    cooler_type - can be either air or liquid cooling (str),
    max_power - maximum power of cpu cooler in watts (int),
    fan_size - fan size of cpu cooler in millimeter (int)
    """
    cooler_name = models.CharField("CPU cooler name", max_length=30)
    COOLER_TYPE = (
        ('air', 'air cooling'),
        ('liquid', 'liquid cooling'),
    )
    cooler_type = models.CharField("CPU cooler type", choices=COOLER_TYPE,
                                   default='air', help_text="CPU cooling type, air or liquid",
                                   max_length=30)
    max_power = models.IntegerField("Max power", help_text="Max CPU cooler power, W")
    fan_size = models.IntegerField("Fan size", help_text="CPU cooler fan size, mm")

    def fan_size_display(self):
        """
        This function adds mm (millimeters) next to
        cooler fan size. returns fan size with mm
        in an f string.
        """
        return f"{self.fan_size}mm"

    fan_size_display.short_description = "FAN SIZE"

    def __str__(self):
        return (f"{self.cooler_name}, {self.cooler_type}, "
                f"{self.max_power}W, {self.fan_size}mm fan size")

    class Meta:
        verbose_name = "CPU cooler"
        verbose_name_plural = 'CPU coolers'
