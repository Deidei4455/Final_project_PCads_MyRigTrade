from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from ..models.part_models import Cpu, Gpu, Psu, Ram

from ..models.part_listing_models import (CpuListing, GpuListing, PsuListing,
                                          RamListing, StorageListing, CasePCListing,
                                          MotherboardListing, CpuCoolerListing)

from ..models.build_with_listing import PcBuild, PcBuildListing, RamBuild, StorageBuild

from ..forms import (UserCpuListingCreateForm, UserPcbuildListingCreateForm, UserGpuListingCreateForm,
                     UserPsuListingCreateForm, UserRamListingCreateForm, UserStorageListingCreateForm,
                     UserCasePCListingCreateForm, UserMotherboardListingCreateForm, UserCpuCoolerListingCreateForm)


class CpuListingByUserCreateView(LoginRequiredMixin, generic.CreateView):
    """
    This class lets users create their own CPU listing.
    """
    model = CpuListing
    form_class = UserCpuListingCreateForm
    template_name = 'user_create_templates/user_cpulisting_form.html'
    success_url = '/pcportal/mylistings'

    def form_valid(self, form):
        cpu = form.cleaned_data['cpu']
        cpu_brand = form.cleaned_data['cpu_brand']
        cpu_model_new = form.cleaned_data['cpu_model_new']
        cpu_cores = form.cleaned_data['cpu_cores']
        cpu_base_speed = form.cleaned_data['cpu_base_speed']
        cpu_socket_type = form.cleaned_data['cpu_socket_type']
        price = form.cleaned_data['price']
        quantity = form.cleaned_data['quantity']

        if not cpu and cpu_brand and cpu_model_new:
            cpu = Cpu.objects.create(
                brand=cpu_brand,
                cpu_model=cpu_model_new,
                cores=cpu_cores,
                base_clock_speed=cpu_base_speed,
                socket_type=cpu_socket_type
            )
        form.instance.cpu = cpu
        form.instance.price = price
        form.instance.quantity = quantity
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class GpuListingByUserCreateView(LoginRequiredMixin, generic.CreateView):
    """
    This view lets users create their own GPU listing.
    """
    model = GpuListing
    form_class = UserGpuListingCreateForm
    template_name = 'user_create_templates/user_gpulisting_form.html'
    success_url = '/pcportal/mylistings'

    def form_valid(self, form):
        gpu = form.cleaned_data['gpu']
        gpu_brand = form.cleaned_data['gpu_brand']
        gpu_model_new = form.cleaned_data['gpu_model_new']
        gpu_vram = form.cleaned_data['gpu_vram']
        gpu_clock_speed = form.cleaned_data['gpu_clock_speed']
        price = form.cleaned_data['price']
        quantity = form.cleaned_data['quantity']

        if not gpu and gpu_brand and gpu_model_new and gpu_vram and gpu_clock_speed:
            gpu = Gpu.objects.create(
                brand=gpu_brand,
                gpu_model=gpu_model_new,
                vram=gpu_vram,
                clock_speed=gpu_clock_speed,
            )
        form.instance.gpu = gpu
        form.instance.price = price
        form.instance.quantity = quantity
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class PsuListingByUserCreateView(LoginRequiredMixin, generic.CreateView):
    """
    This view lets users create their own PSU listing.
    """
    model = PsuListing
    form_class = UserPsuListingCreateForm
    template_name = 'user_create_templates/user_psulisting_form.html'
    success_url = '/pcportal/mylistings'

    def form_valid(self, form):
        psu = form.cleaned_data['psu']
        psu_name = form.cleaned_data['psu_name']
        psu_wattage = form.cleaned_data['psu_wattage']
        efficiency = form.cleaned_data['efficiency']
        price = form.cleaned_data['price']
        quantity = form.cleaned_data['quantity']

        if not psu and psu_name and psu_wattage and efficiency:
            psu = Psu.objects.create(
                psu_name=psu_name,
                wattage=psu_wattage,
                efficiency=efficiency,
            )
        form.instance.psu = psu
        form.instance.price = price
        form.instance.quantity = quantity
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class RamListingByUserCreateView(LoginRequiredMixin, generic.CreateView):
    """
    This view lets users create their own RAM listing.
    """
    model = RamListing
    form_class = UserRamListingCreateForm
    template_name = 'user_create_templates/user_ramlisting_form.html'
    success_url = '/pcportal/mylistings'

    def form_valid(self, form):
        ram = form.cleaned_data['ram']
        ram_name = form.cleaned_data['ram_name']
        ram_capacity = form.cleaned_data['ram_capacity']
        ram_type = form.cleaned_data['ram_type']
        ram_speed = form.cleaned_data['ram_speed']
        price = form.cleaned_data['price']
        quantity = form.cleaned_data['quantity']

        if not ram and ram_name and ram_capacity and ram_speed:
            ram = Ram.objects.create(
                ram_name=ram_name,
                capacity=ram_capacity,
                ram_type=ram_type,
                ram_speed=ram_speed,
            )
        form.instance.ram = ram
        form.instance.price = price
        form.instance.quantity = quantity
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class StorageListingByUserCreateView(LoginRequiredMixin, generic.CreateView):
    """
    This view lets users create their own storage listing.
    """
    model = StorageListing
    form_class = UserStorageListingCreateForm
    template_name = 'user_create_templates/user_storagelisting_form.html'
    success_url = '/pcportal/mylistings'

    def form_valid(self, form):
        storage = form.cleaned_data['storage']
        storage_name = form.cleaned_data['storage_name']
        storage_capacity = form.cleaned_data['storage_capacity']
        storage_type = form.cleaned_data['storage_type']
        write_speed = form.cleaned_data['write_speed']
        read_speed = form.cleaned_data['read_speed']
        price = form.cleaned_data['price']
        quantity = form.cleaned_data['quantity']

        if not storage and storage_name and storage_capacity and write_speed and read_speed:
            storage = Ram.objects.create(
                storage_name=storage_name,
                storage_type=storage_type,
                capacity=storage_capacity,
                write_speed=write_speed,
                read_speed=read_speed,
            )
        form.instance.storage = storage
        form.instance.price = price
        form.instance.quantity = quantity
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class CasePCListingByUserCreateView(LoginRequiredMixin, generic.CreateView):
    """
    This view lets users create their own PC case listing.
    """
    model = CasePCListing
    form_class = UserCasePCListingCreateForm
    template_name = 'user_create_templates/user_casepclisting_form.html'
    success_url = '/pcportal/mylistings'

    def form_valid(self, form):
        casepc = form.cleaned_data['casepc']
        case_name = form.cleaned_data['case_name']
        case_size = form.cleaned_data['case_size']
        price = form.cleaned_data['price']
        quantity = form.cleaned_data['quantity']

        if not casepc and case_name:
            casepc = Ram.objects.create(
                case_name=case_name,
                case_size=case_size,
            )
        form.instance.case = casepc
        form.instance.price = price
        form.instance.quantity = quantity
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class MotherboardListingByUserCreateView(LoginRequiredMixin, generic.CreateView):
    """
    This view lets users create their own motherboard listing.
    """
    model = MotherboardListing
    form_class = UserMotherboardListingCreateForm
    template_name = 'user_create_templates/user_motherboardlisting_form.html'
    success_url = '/pcportal/mylistings'

    def form_valid(self, form):
        motherboard = form.cleaned_data['motherboard']
        motherboard_name = form.cleaned_data['motherboard_name']
        chipset = form.cleaned_data['chipset']
        socket_type = form.cleaned_data['socket_type']
        ram_type = form.cleaned_data['ram_type']
        board_size = form.cleaned_data['board_size']
        max_ram = form.cleaned_data['max_ram']
        price = form.cleaned_data['price']
        quantity = form.cleaned_data['quantity']

        if not motherboard and motherboard_name and chipset and socket_type and max_ram:
            motherboard = Ram.objects.create(
                motherboard_name=motherboard_name,
                chipset=chipset,
                socket_type=socket_type,
                ram_type=ram_type,
                board_size=board_size,
                max_ram=max_ram,
            )
        form.instance.motherboard = motherboard
        form.instance.price = price
        form.instance.quantity = quantity
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class CpuCoolerListingByUserCreateView(LoginRequiredMixin, generic.CreateView):
    """
    This view lets users create their own CPU cooler listing.
    """
    model = CpuCoolerListing
    form_class = UserCpuCoolerListingCreateForm
    template_name = 'user_create_templates/user_cpucoolerlisting_form.html'
    success_url = '/pcportal/mylistings'

    def form_valid(self, form):
        cpucooler = form.cleaned_data['cpucooler']
        cooler_name = form.cleaned_data['cooler_name']
        max_power = form.cleaned_data['max_power']
        fan_size = form.cleaned_data['fan_size']
        cooler_type = form.cleaned_data['cooler_type']
        price = form.cleaned_data['price']
        quantity = form.cleaned_data['quantity']

        if not cpucooler and cooler_name and max_power and fan_size:
            cpucooler = Ram.objects.create(
                cooler_name=cooler_name,
                cooler_type=cooler_type,
                max_power=max_power,
                fan_size=fan_size,
            )
        form.instance.cpucooler = cpucooler
        form.instance.price = price
        form.instance.quantity = quantity
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)


class PcBuildListingByUserCreateView(LoginRequiredMixin, generic.CreateView):
    """
    This class lets users create their own pc build listing.
    """
    model = PcBuildListing
    form_class = UserPcbuildListingCreateForm
    template_name = 'user_create_templates/user_pcbuildlisting_form.html'
    success_url = '/pcportal/mylistings'

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        cpu = form.cleaned_data.get('cpu')
        gpu = form.cleaned_data.get('gpu')
        psu = form.cleaned_data.get('psu')
        motherboard = form.cleaned_data.get('motherboard')
        cpucooler = form.cleaned_data.get('cpucooler')
        casepc = form.cleaned_data.get('casepc')
        ram = form.cleaned_data.get('ram')
        ram_quantity = form.cleaned_data.get('ram_quantity')
        storage = form.cleaned_data.get('storage')
        storage_quantity = form.cleaned_data.get('storage_quantity')
        price = form.cleaned_data.get('price')
        pc_build = PcBuild.objects.create(
            title=title,
            cpu=cpu,
            cpucooler=cpucooler,
            gpu=gpu,
            psu=psu,
            motherboard=motherboard,
            pc_case=casepc,
        )
        RamBuild.objects.create(ram=ram, quantity=ram_quantity, pcbuild=pc_build)
        StorageBuild.objects.create(storage=storage, quantity=storage_quantity, pcbuild=pc_build)

        form.instance.pc_build = pc_build
        form.instance.price = price
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)
