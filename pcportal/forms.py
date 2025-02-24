from django import forms
from django.core.exceptions import ValidationError

from .models import Profile, User, SellerReview
from .models import Cpu, Gpu, Psu, CpuCooler, Motherboard, CasePC, Ram, Storage
from .models import (PcBuildListing, CpuListing, GpuListing, PsuListing, RamListing, StorageListing,
                     CasePCListing, MotherboardListing, CpuCoolerListing)


class SellerReviewForm(forms.ModelForm):
    """
    This form lets a user create a review
    about a seller.
    """

    class Meta:
        model = SellerReview
        fields = ('content', 'seller', 'reviewer')
        widgets = {
            'seller': forms.HiddenInput(),
            'reviewer': forms.HiddenInput(),
        }


class ProfileUpdateForm(forms.ModelForm):
    """
    This form lets a user update their profile picture.
    """

    class Meta:
        model = Profile
        fields = ('picture',)


class UserUpdateForm(forms.ModelForm):
    """
    This form lets a user update their email.
    """

    class Meta:
        model = User
        fields = ('email',)


class DateInput(forms.DateInput):
    input_type = 'date'


# PART LISTINGS CREATE
class UserCpuListingCreateForm(forms.ModelForm):
    """
    This form lets user create their own CPU listing,
    lets them choose a CPU from existing ones or
    enter a new cpu and create a new listing for the
    new cpu. Only one of the 2 options can be done,
    if a cpu is chosen, a new cpu cannot be entered
    and same goes in reverse.
    clean() method makes sure that the user gives the
    right cpu data, checks price and quantity, checks that
    only a cpus is chosen or a new cpu is entered, returns
    cleaned data.
    """
    cpu = forms.ModelChoiceField(queryset=Cpu.objects.all(),
                                 label="Choose a CPU or leave blank for a new one", required=False)

    cpu_brand = forms.CharField(required=False, label="CPU brand if no cpu selected")
    cpu_model_new = forms.CharField(required=False, label="CPU model if no cpu selected")
    cpu_cores = forms.IntegerField(required=False, label="Number of cores in CPU if no cpu selected")
    cpu_base_speed = forms.FloatField(required=False, label="CPU's base clock speed in GHz if no cpu selected")
    cpu_socket_type = forms.CharField(required=False, label="CPU's socket type like AM4, LGA 1151 if no cpu selected")

    price = forms.FloatField(required=True, label="CPU price (price per one CPU)", min_value=1)
    quantity = forms.IntegerField(required=True, label="CPU quantity", min_value=1)

    class Meta:
        model = CpuListing
        fields = ('cpu', 'expiration_date', 'quantity', 'price', 'listing_seller')
        widgets = {
            'expiration_date': DateInput(),
            'listing_seller': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        cpu = cleaned_data.get('cpu')
        cpu_brand = cleaned_data.get('cpu_brand')
        cpu_model_new = cleaned_data.get('cpu_model_new')
        cpu_socket_type = cleaned_data.get('cpu_socket_type')

        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if price < 1 or quantity < 1:
            raise ValidationError("Price and quantity must be 1 or higher numbers")

        if not cpu and (cpu_brand or cpu_model_new or cpu_socket_type):
            if not cpu_brand or not cpu_model_new or not cpu_socket_type:
                raise ValidationError("CPU brand, model and socket type need to be entered entering a new cpu")

        if cpu and (cpu_brand or cpu_model_new or cpu_socket_type):
            raise ValidationError("Can't select a cpu and enter a new cpu together, only one option can be accepted")

        return cleaned_data


class UserGpuListingCreateForm(forms.ModelForm):
    """
    This form lets user create their own GPU listing,
    lets them choose a GPU from existing ones or
    enter a new cpu and create a new listing for the
    new gpu. Only one of the 2 options can be done,
    if a GPU is chosen, a new GPU cannot be entered
    and same goes in reverse.
    clean() method makes sure that the user gives the
    right GPU data, checks price and quantity, checks that
    only a GPU is chosen or a new GPU is entered, returns
    cleaned data.
    """
    gpu = forms.ModelChoiceField(queryset=Gpu.objects.all(),
                                 label="Choose a GPU or leave blank for a new one", required=False)

    gpu_brand = forms.CharField(required=False, label="GPU brand if no GPU selected")
    gpu_model_new = forms.CharField(required=False, label="GPU model if no GPU selected")
    gpu_vram = forms.IntegerField(required=False, label="Number of Vram in GB GPU has if no GPU selected")
    gpu_clock_speed = forms.IntegerField(required=False, label="CPU's clock speed in MHz if no GPU selected")

    price = forms.FloatField(required=True, label="GPU price (price per one GPU)", min_value=1)
    quantity = forms.IntegerField(required=True, label="GPU quantity", min_value=1)

    class Meta:
        model = GpuListing
        fields = ('gpu', 'expiration_date', 'quantity', 'price', 'listing_seller')
        widgets = {
            'expiration_date': DateInput(),
            'listing_seller': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        gpu = cleaned_data.get('gpu')
        gpu_brand = cleaned_data.get('gpu_brand')
        gpu_model_new = cleaned_data.get('gpu_model_new')
        gpu_vram = cleaned_data.get('gpu_vram')
        gpu_clock_speed = cleaned_data.get('gpu_clock_speed')

        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if price < 1 or quantity < 1:
            raise ValidationError("Price and quantity must be 1 or higher numbers")

        if not gpu and (gpu_brand or gpu_model_new or gpu_vram or gpu_clock_speed):
            if not gpu_brand or not gpu_model_new or not gpu_vram or not gpu_clock_speed:
                raise ValidationError("GPU brand, model, vram, clock speed must all be entered")

        if gpu and (gpu_brand or gpu_model_new or gpu_clock_speed or gpu_clock_speed):
            raise ValidationError("Can't select a gpu and enter a new gpu together, "
                                  "only one option can be accepted")

        return cleaned_data


class UserPsuListingCreateForm(forms.ModelForm):
    """
    This form lets user create their own PSU listing,
    lets them choose a PSU from existing ones or
    enter a new PSU and create a new listing for the
    new PSU. Only one of the 2 options can be done,
    if a PSU is chosen, a new PSU cannot be entered
    and same goes in reverse.
    clean() method makes sure that the user gives the
    right PSU data, checks price and quantity, checks that
    only a PSU is chosen or a new PSU is entered, returns
    cleaned data.
    """
    psu = forms.ModelChoiceField(queryset=Psu.objects.all(),
                                 label="Choose a PSU or leave blank for a new one", required=False)

    psu_name = forms.CharField(required=False, label="PSU name if no PSU selected")
    psu_wattage = forms.IntegerField(required=False, label="PSU wattage if no PSU is selected")
    efficiency = forms.ChoiceField(choices=Psu.EFF_RATING,
                                   label="PSU efficiency rating, will NOT change for a selected PSU",
                                   required=False)

    price = forms.FloatField(required=True, label="PSU price (price per one PSU)", min_value=1)
    quantity = forms.IntegerField(required=True, label="PSU quantity", min_value=1)

    class Meta:
        model = PsuListing
        fields = ('psu', 'expiration_date', 'quantity', 'price', 'listing_seller')
        widgets = {
            'expiration_date': DateInput(),
            'listing_seller': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        psu = cleaned_data.get('psu')
        psu_name = cleaned_data.get('psu_name')
        psu_wattage = cleaned_data.get('psu_wattage')
        efficiency = cleaned_data.get('efficiency')

        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if price < 1 or quantity < 1:
            raise ValidationError("Price and quantity must be 1 or higher numbers")

        if not psu and (psu_name or psu_wattage or efficiency):
            if not psu_name or not psu_wattage or not efficiency:
                raise ValidationError("PSU name, wattage, efficiency must all be entered")

        if psu and (psu_name or psu_wattage):
            raise ValidationError("Can't select a psu and enter a new psu together, "
                                  "only one option can be accepted")

        if psu and efficiency:
            cleaned_data['efficiency'] = None

        return cleaned_data


class UserRamListingCreateForm(forms.ModelForm):
    """
    This form lets user create their own RAM listing,
    lets them choose RAM from existing ones or
    enter new RAM and create a new listing for the
    new RAM. Only one of the 2 options can be done,
    if a RAM module is chosen, new RAM cannot be entered
    and same goes in reverse.
    clean() method makes sure that the user gives the
    right RAM data, checks price and quantity, checks that
    only a RAM module is chosen or a new RAM module is entered,
    returns  cleaned data.
    """
    ram = forms.ModelChoiceField(queryset=Ram.objects.all(),
                                 label="Choose RAM or leave blank for new RAM", required=False)

    ram_name = forms.CharField(required=False, label="RAM name if no RAM selected")
    ram_capacity = forms.IntegerField(required=False, label="RAM capacity in GB if no RAM is selected")
    ram_type = forms.ChoiceField(choices=Ram.RAM_TYPE,
                                 label="RAM type, will NOT change for a selected RAM",
                                 required=False)
    ram_speed = forms.IntegerField(required=False, label="RAM wattage if no RAM is selected")

    price = forms.FloatField(required=True, label="RAM price (price per one RAM)", min_value=1)
    quantity = forms.IntegerField(required=True, label="RAM quantity", min_value=1)

    class Meta:
        model = RamListing
        fields = ('ram', 'expiration_date', 'quantity', 'price', 'listing_seller')
        widgets = {
            'expiration_date': DateInput(),
            'listing_seller': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        ram = cleaned_data.get('ram')
        ram_name = cleaned_data.get('ram_name')
        ram_capacity = cleaned_data.get('ram_capacity')
        ram_type = cleaned_data.get('ram_type')
        ram_speed = cleaned_data.get('ram_speed')

        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if price < 1 or quantity < 1:
            raise ValidationError("Price and quantity must be 1 or higher numbers")

        if not ram and (ram_name or ram_capacity or ram_speed):
            if not ram_name or not ram_capacity or not ram_speed:
                raise ValidationError("RAM name, capacity, speed must all be entered")

        if ram and (ram_name or ram_capacity):
            raise ValidationError("Can't select a RAM and enter a new RAM together, "
                                  "only one option can be accepted")

        if ram and ram_type:
            cleaned_data['ram_type'] = None

        return cleaned_data


class UserStorageListingCreateForm(forms.ModelForm):
    """
    This form lets user create their own storage listing,
    lets them choose a storage from existing ones or
    enter a new storage and create a new listing for the
    new storage. Only one of the 2 options can be done,
    if a storage device is chosen, a new storage cannot be entered
    and same goes in reverse.
    clean() method makes sure that the user gives the
    right storage data, checks price and quantity, checks that
    only a storage is chosen or a new storage is entered, returns
    cleaned data.
    """
    storage = forms.ModelChoiceField(queryset=Storage.objects.all(),
                                     label="Choose storage or leave blank for new storage", required=False)

    storage_name = forms.CharField(required=False, label="storage name if no storage selected")
    storage_capacity = forms.IntegerField(required=False, label="storage capacity in GB if no storage is selected")
    storage_type = forms.ChoiceField(choices=Storage.STORAGE_TYPE,
                                     label="storage type, will NOT change for selected storage",
                                     required=False)
    write_speed = forms.IntegerField(required=False, label="write speed if no storage is selected")
    read_speed = forms.IntegerField(required=False, label="read speed if no storage is selected")

    price = forms.FloatField(required=True, label="storage price (price per storage)", min_value=1)
    quantity = forms.IntegerField(required=True, label="storage quantity", min_value=1)

    class Meta:
        model = StorageListing
        fields = ('storage', 'expiration_date', 'quantity', 'price', 'listing_seller')
        widgets = {
            'expiration_date': DateInput(),
            'listing_seller': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        storage = cleaned_data.get('storage')
        storage_name = cleaned_data.get('storage_name')
        storage_capacity = cleaned_data.get('storage_capacity')
        storage_type = cleaned_data.get('storage_type')
        write_speed = cleaned_data.get('write_speed')
        read_speed = cleaned_data.get('read_speed')

        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if price < 1 or quantity < 1:
            raise ValidationError("Price and quantity must be 1 or higher numbers")

        if not storage and (storage_name or storage_capacity or write_speed or read_speed):
            if not storage_name or not storage_capacity or not write_speed or not read_speed:
                raise ValidationError("storage name, capacity, speed must all be entered")

        if storage and (storage_name or storage_capacity or write_speed or read_speed):
            raise ValidationError("Can't select a storage and enter a new storage together, "
                                  "only one option can be accepted")

        if storage and storage_type:
            cleaned_data['storage_type'] = None

        return cleaned_data


class UserCasePCListingCreateForm(forms.ModelForm):
    """
    This form lets user create their own PC case listing,
    lets them choose a PC case from existing ones or
    enter a new PC case and create a new listing for the
    new PC case. Only one of the 2 options can be done,
    if a PC case is chosen, a new PC case cannot be entered
    and same goes in reverse.
    clean() method makes sure that the user gives the
    right PC case data, checks price and quantity, checks that
    only a PC case is chosen or a new PC case is entered, returns
    cleaned data.
    """
    casepc = forms.ModelChoiceField(queryset=CasePC.objects.all(),
                                    label="Choose a PC case or leave blank for a new one", required=False)

    case_name = forms.CharField(required=False, label="PC case name if no PC case selected")
    case_size = forms.ChoiceField(choices=CasePC.CASE_SIZE,
                                  label="PC case size, will NOT change for selected one",
                                  required=False)

    price = forms.FloatField(required=True, label="PC case price (price per PC case)", min_value=1)
    quantity = forms.IntegerField(required=True, label="PC case quantity", min_value=1)

    class Meta:
        model = CasePCListing
        fields = ('casepc', 'expiration_date', 'quantity', 'price', 'listing_seller')
        widgets = {
            'expiration_date': DateInput(),
            'listing_seller': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        casepc = cleaned_data.get('casepc')
        case_name = cleaned_data.get('case_name')
        case_size = cleaned_data.get('case_size')

        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if price < 1 or quantity < 1:
            raise ValidationError("Price and quantity must be 1 or higher numbers")

        if not casepc and case_name:
            if not case_name:
                raise ValidationError("PC case name be entered")

        if casepc and case_name:
            raise ValidationError("Can't select a PC case and enter PC case name together, "
                                  "only one option can be accepted")

        if casepc and case_size:
            cleaned_data['case_size'] = None

        return cleaned_data


class UserMotherboardListingCreateForm(forms.ModelForm):
    """
    This form lets user create their own motherboard listing,
    lets them choose a motherboard from existing ones or
    enter a new motherboard and create a new listing for the
    new motherboard. Only one of the 2 options can be done,
    if a motherboard is chosen, a new motherboard cannot be entered
    and same goes in reverse.
    clean() method makes sure that the user gives the
    right motherboard data, checks price and quantity, checks that
    only a motherboard is chosen or a new motherboard is entered, returns
    cleaned data.
    """
    motherboard = forms.ModelChoiceField(queryset=Motherboard.objects.all(),
                                         label="Choose motherboard or leave blank for a new one", required=False)

    motherboard_name = forms.CharField(required=False, label="Motherboard name if no motherboard selected")
    chipset = forms.CharField(required=False, label="Motherboard chipset type if no motherboard is selected")
    socket_type = forms.CharField(required=False, label="Socket type if no motherboard is selected")
    ram_type = forms.ChoiceField(choices=Motherboard.RAM_TYPE,
                                 label="RAM type, will NOT change for selected motherboard",
                                 required=False)
    board_size = forms.ChoiceField(choices=Motherboard.BOARD_SIZE,
                                   label="Board size, will NOT change for selected motherboard",
                                   required=False)
    max_ram = forms.IntegerField(required=False, label="Maximum ram capacity in GB if no motherboard selected")

    price = forms.FloatField(required=True, label="motherboard price (price per motherboard)", min_value=1)
    quantity = forms.IntegerField(required=True, label="motherboard quantity", min_value=1)

    class Meta:
        model = MotherboardListing
        fields = ('motherboard', 'expiration_date', 'quantity', 'price', 'listing_seller')
        widgets = {
            'expiration_date': DateInput(),
            'listing_seller': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        motherboard = cleaned_data.get('motherboard')
        motherboard_name = cleaned_data.get('motherboard_name')
        chipset = cleaned_data.get('chipset')
        socket_type = cleaned_data.get('socket_type')
        ram_type = cleaned_data.get('ram_type')
        board_size = cleaned_data.get('board_size')
        max_ram = cleaned_data.get('max_ram')

        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if price < 1 or quantity < 1:
            raise ValidationError("Price and quantity must be 1 or higher numbers")

        if not motherboard and (motherboard_name or chipset or socket_type or max_ram):
            if not motherboard_name or not chipset or not socket_type or not max_ram:
                raise ValidationError("motherboard name, chipset, socket type, max ram must all be entered")

        if motherboard and (motherboard_name or chipset or socket_type or max_ram):
            raise ValidationError("Can't select a motherboard and enter a new motherboard together, "
                                  "only one option can be accepted")

        if motherboard and (ram_type or board_size):
            cleaned_data['ram_type'] = None
            cleaned_data['board_size'] = None

        return cleaned_data


class UserCpuCoolerListingCreateForm(forms.ModelForm):
    """
    This form lets user create their own CPU cooler listing,
    lets them choose a CPU cooler from existing ones or
    enter a new CPU cooler and create a new listing for the
    new CPU cooler. Only one of the 2 options can be done,
    if a CPU cooler chosen, a new CPU cooler cannot be entered
    and same goes in reverse.
    clean() method makes sure that the user gives the
    right CPU cooler data, checks price and quantity, checks that
    only a CPU cooler is chosen or a new CPU cooler is entered, returns
    cleaned data.
    """
    cpucooler = forms.ModelChoiceField(queryset=CpuCooler.objects.all(),
                                       label="Choose CPU cooler or leave blank for a new one", required=False)

    cooler_name = forms.CharField(required=False,
                                  label="CPU cooler name if no CPU cooler selected")
    max_power = forms.IntegerField(required=False,
                                   label="CPU cooler's max power in W type if no CPU cooler is selected")
    fan_size = forms.IntegerField(required=False,
                                  label="CPU cooler's fan size in mm if no CPU cooler is selected")
    cooler_type = forms.ChoiceField(choices=CpuCooler.COOLER_TYPE,
                                    label="CPU cooler type, will NOT change for selected CPU cooler")

    price = forms.FloatField(required=True,
                             label="CPU cooler price (price per CPU cooler)", min_value=1)
    quantity = forms.IntegerField(required=True, label="CPU cooler quantity", min_value=1)

    class Meta:
        model = CpuCoolerListing
        fields = ('cpucooler', 'expiration_date', 'quantity', 'price', 'listing_seller')
        widgets = {
            'expiration_date': DateInput(),
            'listing_seller': forms.HiddenInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        cpucooler = cleaned_data.get('cpucooler')
        cooler_name = cleaned_data.get('cooler_name')
        max_power = cleaned_data.get('max_power')
        fan_size = cleaned_data.get('fan_size')
        cooler_type = cleaned_data.get('cooler_type')

        price = cleaned_data.get('price')
        quantity = cleaned_data.get('quantity')

        if price < 1 or quantity < 1:
            raise ValidationError("Price and quantity must be 1 or higher numbers")

        if not cpucooler and (cooler_name or max_power or fan_size):
            if not cooler_name or not max_power or not fan_size:
                raise ValidationError("CPU cooler name, power, fans size, type must all be entered")

        if cpucooler and (cooler_name or max_power or fan_size):
            raise ValidationError("Can't select a CPU cooler and enter a new CPU cooler together, "
                                  "only one option can be accepted")

        if cpucooler and cooler_type:
            cleaned_data['cooler_type'] = None

        return cleaned_data


# PC BUILD LISTING

class UserPcbuildListingCreateForm(forms.ModelForm):
    """
    This form lets user create their own PC build listing,
    lets them choose parts from existing ones.
    Some parts can be skipped and not chosen.
    clean() method makes sure that the user gives the
    right information, it is mostly done in create view.
    """
    title = forms.CharField(required=True, label="PC build title")
    cpu = forms.ModelChoiceField(queryset=Cpu.objects.all(), label="Choose a CPU", required=True)
    gpu = forms.ModelChoiceField(queryset=Gpu.objects.all(), label="Choose a GPU", required=False)
    psu = forms.ModelChoiceField(queryset=Psu.objects.all(), label="Choose a PSU", required=True)
    motherboard = forms.ModelChoiceField(queryset=Motherboard.objects.all(),
                                         label="Choose a Motherboard", required=True)
    cpucooler = forms.ModelChoiceField(queryset=CpuCooler.objects.all(),
                                       label="Choose a CPU cooler", required=False)
    casepc = forms.ModelChoiceField(queryset=CasePC.objects.all(), label="Choose a PC case", required=True)

    ram = forms.ModelChoiceField(queryset=Ram.objects.all(), label="Select RAM", required=True)
    ram_quantity = forms.IntegerField(min_value=1, max_value=4, required=True,
                                      label="Quantity of RAM sticks")
    storage = forms.ModelChoiceField(queryset=Storage.objects.all(), label="Select storage", required=True)
    storage_quantity = forms.IntegerField(min_value=1, required=True,
                                          label="How many storage devices will there be")

    price = forms.FloatField(required=True, label="PC build price", min_value=1)
    condition = forms.ChoiceField(choices=PcBuildListing.PC_CONDITION,
                                  label="PC build condition", required=True)

    class Meta:
        model = PcBuildListing
        fields = ('title', 'price', 'expiration_date', 'condition', 'description', 'cpu', 'listing_seller',
                  'gpu', 'psu', 'motherboard', 'cpucooler', 'casepc', 'ram', 'ram_quantity', 'storage',
                  'storage_quantity')
        widgets = {
            'expiration_date': DateInput(),
            'listing_seller': forms.HiddenInput(),
            'description': forms.Textarea(),
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
