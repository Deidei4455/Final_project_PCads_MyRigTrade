from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator

from django.db.models import Q

from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models.seller_model import Seller
from .models.part_models import Cpu, Gpu, Psu, Ram, Storage, CasePC, Motherboard, CpuCooler
from .models.part_listing_models import (CpuListing, GpuListing, PsuListing,
                                         RamListing, StorageListing, CasePCListing,
                                         MotherboardListing, CpuCoolerListing)
from .models.build_with_listing import PcBuild, PcBuildListing
from .forms import ProfileUpdateForm, UserUpdateForm, User
from .utils import check_password


#  main
def index(request):
    """
    This function handles rendering of homepage,
    calculate how many parts, part listings, pc build
    listings, pc builds and sellers are the in database,
    it also counts how many time a visitor has visited
    the site.
    """
    total_parts_count = (Cpu.objects.count() + Gpu.objects.count() + Psu.objects.count()
                         + Ram.objects.count() + Storage.objects.count() + CasePC.objects.count()
                         + Motherboard.objects.count() + CpuCooler.objects.count())

    total_part_listings = (CpuListing.objects.count() + GpuListing.objects.count()
                           + PsuListing.objects.count() + RamListing.objects.count()
                           + StorageListing.objects.count() + CasePCListing.objects.count()
                           + MotherboardListing.objects.count() + CpuCoolerListing.objects.count())

    num_pc_builds = PcBuild.objects.count()
    num_pc_build_listings = PcBuildListing.objects.count()

    num_sellers = Seller.objects.count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context_my = {
        'num_parts': total_parts_count,
        'num_listings': total_part_listings,
        'num_pc_builds': num_pc_builds,
        'num_pc_build_listings': num_pc_build_listings,
        'num_sellers': num_sellers,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context_my)


#  all model views in lists

def get_all_parts(request):
    """
    This function retrieves all parts
    and renders them in all parts page.
    """
    cpu_list = Cpu.objects.all()
    gpu_list = Gpu.objects.all()
    psu_list = Psu.objects.all()
    ram_list = Ram.objects.all()
    storage_list = Storage.objects.all()
    casepc_list = CasePC.objects.all()
    motherboard_list = Motherboard.objects.all()
    cpucooler_list = CpuCooler.objects.all()

    tab = request.GET.get('tab', 'cpu')
    page_number = request.GET.get('page')

    paged_cpu_list = (Paginator(cpu_list, 6)).get_page(page_number)
    paged_gpu_list = (Paginator(gpu_list, 6)).get_page(page_number)
    paged_psu_list = (Paginator(psu_list, 6)).get_page(page_number)
    paged_ram_list = (Paginator(ram_list, 6)).get_page(page_number)
    paged_storage_list = (Paginator(storage_list, 6)).get_page(page_number)
    paged_casepc_list = (Paginator(casepc_list, 6)).get_page(page_number)
    paged_motherboard_list = (Paginator(motherboard_list, 6)).get_page(page_number)
    paged_cpucooler_list = (Paginator(cpucooler_list, 6)).get_page(page_number)

    context_my = {
        'cpu_list': paged_cpu_list,
        'gpu_list': paged_gpu_list,
        'psu_list': paged_psu_list,
        'ram_list': paged_ram_list,
        'storage_list': paged_storage_list,
        'casepc_list': paged_casepc_list,
        'motherboard_list': paged_motherboard_list,
        'cpucooler_list': paged_cpucooler_list,
        'active_tab': tab
    }
    return render(request, 'parts.html', context=context_my)


def get_part_listings(request):
    """
    This function retrieves all part listings
    and renders them in all part listings page.
    """
    cpu_listings = CpuListing.objects.all()
    gpu_listings = GpuListing.objects.all()
    psu_listings = PsuListing.objects.all()
    ram_listings = RamListing.objects.all()
    storage_listings = StorageListing.objects.all()
    casepc_listings = CasePCListing.objects.all()
    motherboard_listings = MotherboardListing.objects.all()
    cpucooler_listings = CpuCoolerListing.objects.all()

    tab = request.GET.get('tab', 'cpu')
    page_number = request.GET.get('page')

    paged_cpu_listings = (Paginator(cpu_listings, 6)).get_page(page_number)
    paged_gpu_listings = (Paginator(gpu_listings, 6)).get_page(page_number)
    paged_psu_listings = (Paginator(psu_listings, 6)).get_page(page_number)
    paged_ram_listings = (Paginator(ram_listings, 6)).get_page(page_number)
    paged_storage_listings = (Paginator(storage_listings, 6)).get_page(page_number)
    paged_casepc_listings = (Paginator(casepc_listings, 6)).get_page(page_number)
    paged_motherboard_listings = (Paginator(motherboard_listings, 6)).get_page(page_number)
    paged_cpucooler_listings = (Paginator(cpucooler_listings, 6)).get_page(page_number)

    context_my = {
        'cpu_listings': paged_cpu_listings,
        'gpu_listings': paged_gpu_listings,
        'psu_listings': paged_psu_listings,
        'ram_listings': paged_ram_listings,
        'storage_listings': paged_storage_listings,
        'casepc_listings': paged_casepc_listings,
        'motherboard_listings': paged_motherboard_listings,
        'cpucooler_listings': paged_cpucooler_listings,
        'active_tab': tab,
    }
    return render(request, 'part_listings.html', context=context_my)


class PcBuildListingListView(generic.ListView):
    """
    This class retrieves Pc build listings
    and renders them in pc build listings page.
    """
    model = PcBuildListing
    context_object_name = 'pcbuildlistings'
    template_name = 'pcbuild_listings.html'
    paginate_by = 6


class SellerListView(generic.ListView):
    """
    This class retrieves a list of all sellers
    and renders them in all sellers list page.
    """
    model = Seller
    context_object_name = "sellers_list"
    template_name = "sellers.html"
    paginate_by = 6


def get_seller_listings(request, seller_id):
    """
    This function uses seller's id to filter
    all listings by seller and then displays
    all of that seller's listings.
    """
    one_seller = get_object_or_404(Seller, pk=seller_id)
    seller_pcbuild_listings = PcBuildListing.objects.filter(seller=one_seller)
    seller_cpu_listings = CpuListing.objects.filter(seller=one_seller)
    seller_gpu_listings = GpuListing.objects.filter(seller=one_seller)
    seller_psu_listings = PsuListing.objects.filter(seller=one_seller)
    seller_ram_listings = RamListing.objects.filter(seller=one_seller)
    seller_storage_listings = StorageListing.objects.filter(seller=one_seller)
    seller_casepc_listings = CasePCListing.objects.filter(seller=one_seller)
    seller_motherboard_listings = MotherboardListing.objects.filter(seller=one_seller)
    seller_cpucooler_listings = CpuCoolerListing.objects.filter(seller=one_seller)

    context = {'seller': one_seller,
               'cpu_listings': seller_cpu_listings,
               'gpu_listings': seller_gpu_listings,
               'psu_listings': seller_psu_listings,
               'ram_listings': seller_ram_listings,
               'storage_listings': seller_storage_listings,
               'casepc_listings': seller_casepc_listings,
               'motherboard_listings': seller_motherboard_listings,
               'cpucooler_listings': seller_cpucooler_listings,
               'pcbuild_listings': seller_pcbuild_listings,
               }
    return render(request, 'seller_listings.html', context=context)


#  Individual model views

def get_one_seller(request, seller_id):
    """
    This function uses seller's id to
    get a specific seller by id and then
    renders that seller in a page.
    """
    one_seller = get_object_or_404(Seller, pk=seller_id)

    context = {'seller': one_seller}
    return render(request, 'seller.html', context=context)


class CpuListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific cpu listing and renders it in
    a page.
    """
    model = CpuListing
    context_object_name = 'cpu_listing'
    template_name = 'listing_cpu.html'


class GpuListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific gpu listing and renders it in
    a page.
    """
    model = GpuListing
    context_object_name = 'gpu_listing'
    template_name = 'listing_gpu.html'


class PsuListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific psu listing and renders it in
    a page.
    """
    model = PsuListing
    context_object_name = 'psu_listing'
    template_name = 'listing_psu.html'


class RamListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific ram listing and renders it in
    a page.
    """
    model = RamListing
    context_object_name = 'ram_listing'
    template_name = 'listing_ram.html'


class StorageListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific storage listing and renders it in
    a page.
    """
    model = StorageListing
    context_object_name = 'storage_listing'
    template_name = 'listing_storage.html'


class CasePCListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific pc case listing and renders it in
    a page.
    """
    model = CasePCListing
    context_object_name = 'casepc_listing'
    template_name = 'listing_casepc.html'


class MotherboardListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific motherboard listing and renders it in
    a page.
    """
    model = MotherboardListing
    context_object_name = 'motherboard_listing'
    template_name = 'listing_motherboard.html'


class CpuCoolerListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific cpu cooler listing and renders it in
    a page.
    """
    model = CpuCoolerListing
    context_object_name = 'cpucooler_listing'
    template_name = 'listing_cpucooler.html'


class PcBuildListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific pc build listing and renders it in
    a page.
    """
    model = PcBuildListing
    context_object_name = 'pcbuildlisting'
    template_name = 'listing_pcbuild.html'


# search views

def search_seller(request):
    """
    This function uses search text to filter
    sellers by first name, last name or email
    and returns all search results in a page.
    """
    query_text = request.GET.get('search_text')
    sellers_list = Seller.objects.filter(Q(f_name__icontains=query_text) |
                                         Q(l_name__icontains=query_text) |
                                         Q(email__icontains=query_text))
    search_count = sellers_list.count()

    context = {'query_text': query_text,
               'sellers_list': sellers_list,
               'search_count': search_count
               }

    return render(request, 'search_seller.html', context=context)


def search_pcbuildlisting(request):
    """
    This function uses search text to filter
    pc build listings by pc build title, cpu
    brand, cpu model, gpu brand or model, seller's
    first name and returns all search results.
    It can also filter by min or max prices.
    """
    query_text = request.GET.get('search_text')

    query_min_price = request.GET.get('min_price')
    query_max_price = request.GET.get('max_price')

    pcbuildlisting_list = PcBuildListing.objects.filter(Q(pc_build__title__icontains=query_text) |
                                                        Q(pc_build__cpu__brand__icontains=query_text) |
                                                        Q(pc_build__gpu__brand__icontains=query_text) |
                                                        Q(pc_build__gpu__gpu_model__icontains=query_text) |
                                                        Q(pc_build__cpu__cpu_model__icontains=query_text) |
                                                        Q(seller__f_name__icontains=query_text))

    if query_min_price:
        pcbuildlisting_list = pcbuildlisting_list.filter(price__gte=query_min_price)

    if query_max_price:
        pcbuildlisting_list = pcbuildlisting_list.filter(price__lte=query_max_price)

    search_count = pcbuildlisting_list.count()

    context = {'query_text': query_text,
               'pcbuildlistings': pcbuildlisting_list,
               'search_count': search_count
               }

    return render(request, 'search_pcbuildlisting.html', context=context)


def search_part_listings_by_price(request):
    """
    This function retrieves all part listings
    filtered by minimum or maximum prices
    and renders them in all part listings page
    by price.
    """

    query_min_price = request.GET.get('min_price')
    query_max_price = request.GET.get('max_price')

    cpu_listings = CpuListing.objects.all()
    gpu_listings = GpuListing.objects.all()
    psu_listings = PsuListing.objects.all()
    ram_listings = RamListing.objects.all()
    storage_listings = StorageListing.objects.all()
    casepc_listings = CasePCListing.objects.all()
    motherboard_listings = MotherboardListing.objects.all()
    cpucooler_listings = CpuCoolerListing.objects.all()

    if query_min_price:
        cpu_listings = CpuListing.objects.filter(price__gte=query_min_price)
        gpu_listings = GpuListing.objects.filter(price__gte=query_min_price)
        psu_listings = PsuListing.objects.filter(price__gte=query_min_price)
        ram_listings = RamListing.objects.filter(price__gte=query_min_price)
        storage_listings = StorageListing.objects.filter(price__gte=query_min_price)
        casepc_listings = CasePCListing.objects.filter(price__gte=query_min_price)
        motherboard_listings = MotherboardListing.objects.filter(price__gte=query_min_price)
        cpucooler_listings = CpuCoolerListing.objects.filter(price__gte=query_min_price)

    if query_max_price:
        cpu_listings = CpuListing.objects.filter(price__lte=query_max_price)
        gpu_listings = GpuListing.objects.filter(price__lte=query_max_price)
        psu_listings = PsuListing.objects.filter(price__lte=query_max_price)
        ram_listings = RamListing.objects.filter(price__lte=query_max_price)
        storage_listings = StorageListing.objects.filter(price__lte=query_max_price)
        casepc_listings = CasePCListing.objects.filter(price__lte=query_max_price)
        motherboard_listings = MotherboardListing.objects.filter(price__lte=query_max_price)
        cpucooler_listings = CpuCoolerListing.objects.filter(price__lte=query_max_price)

    tab = request.GET.get('tab', 'cpu')
    page_number = request.GET.get('page')

    paged_cpu_listings = (Paginator(cpu_listings, 6)).get_page(page_number)
    paged_gpu_listings = (Paginator(gpu_listings, 6)).get_page(page_number)
    paged_psu_listings = (Paginator(psu_listings, 6)).get_page(page_number)
    paged_ram_listings = (Paginator(ram_listings, 6)).get_page(page_number)
    paged_storage_listings = (Paginator(storage_listings, 6)).get_page(page_number)
    paged_casepc_listings = (Paginator(casepc_listings, 6)).get_page(page_number)
    paged_motherboard_listings = (Paginator(motherboard_listings, 6)).get_page(page_number)
    paged_cpucooler_listings = (Paginator(cpucooler_listings, 6)).get_page(page_number)

    context_my = {
        'cpu_listings': paged_cpu_listings,
        'gpu_listings': paged_gpu_listings,
        'psu_listings': paged_psu_listings,
        'ram_listings': paged_ram_listings,
        'storage_listings': paged_storage_listings,
        'casepc_listings': paged_casepc_listings,
        'motherboard_listings': paged_motherboard_listings,
        'cpucooler_listings': paged_cpucooler_listings,
        'active_tab': tab,
    }
    return render(request, 'part_listings_by_price.html', context=context_my)


#  user listings view
@login_required
def get_user_listings(request):
    """
    This function retrieves all pc build and
    part listings that belong to the user
    and renders them in user's listings page.
    """

    user = request.user

    cpu_listings = CpuListing.objects.filter(listing_seller=user)
    gpu_listings = GpuListing.objects.filter(listing_seller=user)
    psu_listings = PsuListing.objects.filter(listing_seller=user)
    ram_listings = RamListing.objects.filter(listing_seller=user)
    storage_listings = StorageListing.objects.filter(listing_seller=user)
    casepc_listings = CasePCListing.objects.filter(listing_seller=user)
    motherboard_listings = MotherboardListing.objects.filter(listing_seller=user)
    cpucooler_listings = CpuCoolerListing.objects.filter(listing_seller=user)
    pcbuild_listings = PcBuildListing.objects.filter(listing_seller=user)

    context_my = {
        'cpu_listings': cpu_listings,
        'gpu_listings': gpu_listings,
        'psu_listings': psu_listings,
        'ram_listings': ram_listings,
        'storage_listings': storage_listings,
        'casepc_listings': casepc_listings,
        'motherboard_listings': motherboard_listings,
        'cpucooler_listings': cpucooler_listings,
        'pcbuild_listings': pcbuild_listings,
    }
    return render(request, 'mylistings.html', context=context_my)


#  User registration view
@csrf_protect
def register_user(request):
    """
    This functions lets users get registered
    and shows a message if registration was
    successful or not.
    """
    if request.method == 'GET':
        return render(request, 'registration/registration.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        phone_num = request.POST.get('phone_num')

        if not check_password(password):
            messages.error(request, 'Password must be longer than 5 symbols')
            return redirect('register')

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, f"User with {username} already exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, f"{email} is already taken")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email,
                                        password=password, first_name=f_name, last_name=l_name)
        Seller.objects.create(user=user, f_name=f_name, l_name=l_name, email=email, phone_num=phone_num)

        messages.info(request, f"User {username} has been registered")
        return redirect('login')


#  User profile view
@login_required()
def get_user_profile(request):
    """
    This function renders a profile page,
    it contains information about the user,
    only logged in users can check their own profiles.
    """
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.info(request, 'Profile updated')
        else:
            messages.error(request, 'Profile not updated')
        return redirect('user-profile')

    p_form = ProfileUpdateForm(instance=request.user.profile)
    u_form = UserUpdateForm(instance=request.user)

    return render(request, 'profile.html', context={
        'p_form': p_form,
        'u_form': u_form
    })


# listings by user delete views

class CpuListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = CpuListing
    template_name = 'user_cpulisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'cpu_listing'

    def test_func(self):
        cpulisting_object = self.get_object()
        return cpulisting_object.listing_seller == self.request.user


class GpuListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = GpuListing
    template_name = 'user_gpulisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'gpu_listing'

    def test_func(self):
        gpulisting_object = self.get_object()
        return gpulisting_object.listing_seller == self.request.user


class PsuListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = PsuListing
    template_name = 'user_psulisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'psu_listing'

    def test_func(self):
        psulisting_object = self.get_object()
        return psulisting_object.listing_seller == self.request.user


class RamListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = RamListing
    template_name = 'user_ramlisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'ram_listing'

    def test_func(self):
        ramlisting_object = self.get_object()
        return ramlisting_object.listing_seller == self.request.user


class StorageListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = StorageListing
    template_name = 'user_storagelisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'storage_listing'

    def test_func(self):
        storagelisting_object = self.get_object()
        return storagelisting_object.listing_seller == self.request.user


class CasePCListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = CasePCListing
    template_name = 'user_casepclisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'casepc_listing'

    def test_func(self):
        casepclisting_object = self.get_object()
        return casepclisting_object.listing_seller == self.request.user


class MotherboardListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = MotherboardListing
    template_name = 'user_motherboardlisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'motherboard_listing'

    def test_func(self):
        motherboardlisting_object = self.get_object()
        return motherboardlisting_object.listing_seller == self.request.user


class CpuCoolerListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = CpuCoolerListing
    template_name = 'user_cpucoolerlisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'cpucooler_listing'

    def test_func(self):
        cpucoolerlisting_object = self.get_object()
        return cpucoolerlisting_object.listing_seller == self.request.user


class PcBuildListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = PcBuildListing
    template_name = 'user_pcbuildlisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'pcbuildlisting'

    def test_func(self):
        pcbuildlisting_object = self.get_object()
        return pcbuildlisting_object.listing_seller == self.request.user
