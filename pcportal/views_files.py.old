from django.shortcuts import render, redirect, get_object_or_404, reverse
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

from .models.build_with_listing import PcBuild, PcBuildListing, RamBuild, StorageBuild, UserLikes

from .forms import (ProfileUpdateForm, UserUpdateForm, User, UserCpuListingCreateForm,
                    UserPcbuildListingCreateForm, SellerReviewForm, UserGpuListingCreateForm,
                    UserPsuListingCreateForm, UserRamListingCreateForm, UserStorageListingCreateForm,
                    UserCasePCListingCreateForm, UserMotherboardListingCreateForm, UserCpuCoolerListingCreateForm)

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

    cpus_listings = CpuListing.objects.all()
    total_price_cpus = 0
    cpu_listing_count = 0
    for listing in cpus_listings:
        total_price_cpus += listing.price * listing.quantity
        cpu_listing_count += listing.quantity

    total_price_cpus_avg = total_price_cpus / cpu_listing_count

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
        'num_visits': num_visits,
        'total_price': total_price_cpus,
        'total_price_cpus_avg': round(total_price_cpus_avg, 2),
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            for listing in context['pcbuildlistings']:
                listing.user_liked = listing.likes.filter(user=user).exists()
        return context


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

class SellerDetailView(generic.edit.FormMixin, generic.DetailView):
    """
    This class uses seller's primary key to
    gets a specific seller by it and then
    renders that seller in a page.
    """
    model = Seller
    context_object_name = "seller"
    template_name = "seller.html"
    form_class = SellerReviewForm
    seller_object = None

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.seller_object = self.get_object()
        form.instance.seller = self.get_object()
        form.instance.reviewer = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('seller-one', kwargs={'pk': self.seller_object.id})


class CpuListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific cpu listing and renders it in
    a page.
    """
    model = CpuListing
    context_object_name = 'cpu_listing'
    template_name = 'one_listing_templates/listing_cpu.html'


class GpuListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific gpu listing and renders it in
    a page.
    """
    model = GpuListing
    context_object_name = 'gpu_listing'
    template_name = 'one_listing_templates/listing_gpu.html'


class PsuListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific psu listing and renders it in
    a page.
    """
    model = PsuListing
    context_object_name = 'psu_listing'
    template_name = 'one_listing_templates/listing_psu.html'


class RamListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific ram listing and renders it in
    a page.
    """
    model = RamListing
    context_object_name = 'ram_listing'
    template_name = 'one_listing_templates/listing_ram.html'


class StorageListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific storage listing and renders it in
    a page.
    """
    model = StorageListing
    context_object_name = 'storage_listing'
    template_name = 'one_listing_templates/listing_storage.html'


class CasePCListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific pc case listing and renders it in
    a page.
    """
    model = CasePCListing
    context_object_name = 'casepc_listing'
    template_name = 'one_listing_templates/listing_casepc.html'


class MotherboardListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific motherboard listing and renders it in
    a page.
    """
    model = MotherboardListing
    context_object_name = 'motherboard_listing'
    template_name = 'one_listing_templates/listing_motherboard.html'


class CpuCoolerListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific cpu cooler listing and renders it in
    a page.
    """
    model = CpuCoolerListing
    context_object_name = 'cpucooler_listing'
    template_name = 'one_listing_templates/listing_cpucooler.html'


class PcBuildListingDetailView(generic.DetailView):
    """
    This class retrieves information about
    a specific pc build listing and renders it in
    a page.
    """
    model = PcBuildListing
    context_object_name = 'pcbuildlisting'
    template_name = 'one_listing_templates/listing_pcbuild.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        listing = context['pcbuildlisting']
        if user.is_authenticated:
            listing.user_liked = listing.likes.filter(user=user).exists()
        return context


# search views

def search_seller(request):
    """
    This function uses search text to filter
    sellers by first name, last name or email
    and returns all search results in a page.
    """
    query_text = request.GET.get('search_text')
    if not query_text:
        return redirect("sellers-all")
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

    if not query_text and not query_min_price and not query_max_price:
        return redirect('pcbuild-listings')

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
               'search_count': search_count,
               'query_min_price': query_min_price,
               'query_max_price': query_max_price,
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

    if not query_min_price and not query_max_price:
        return redirect('part-listings')

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
        'query_min_price': query_min_price,
        'query_max_price': query_max_price,
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
    """
    This class lets users delete their own CPU listing.
    """
    model = CpuListing
    template_name = 'user_delete_templates/user_cpulisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'cpu_listing'

    def test_func(self):
        cpulisting_object = self.get_object()
        return cpulisting_object.listing_seller == self.request.user


class GpuListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This class lets users delete their own GPU listing.
    """
    model = GpuListing
    template_name = 'user_delete_templates/user_gpulisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'gpu_listing'

    def test_func(self):
        gpulisting_object = self.get_object()
        return gpulisting_object.listing_seller == self.request.user


class PsuListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This class lets users delete their own PSU listing.
    """
    model = PsuListing
    template_name = 'user_delete_templates/user_psulisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'psu_listing'

    def test_func(self):
        psulisting_object = self.get_object()
        return psulisting_object.listing_seller == self.request.user


class RamListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This class lets users delete their own RAM listing.
    """
    model = RamListing
    template_name = 'user_delete_templates/user_ramlisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'ram_listing'

    def test_func(self):
        ramlisting_object = self.get_object()
        return ramlisting_object.listing_seller == self.request.user


class StorageListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This class lets users delete their own Storage device listing.
    """
    model = StorageListing
    template_name = 'user_delete_templates/user_storagelisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'storage_listing'

    def test_func(self):
        storagelisting_object = self.get_object()
        return storagelisting_object.listing_seller == self.request.user


class CasePCListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This class lets users delete their own PC case listing.
    """
    model = CasePCListing
    template_name = 'user_delete_templates/user_casepclisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'casepc_listing'

    def test_func(self):
        casepclisting_object = self.get_object()
        return casepclisting_object.listing_seller == self.request.user


class MotherboardListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This class lets users delete their own motherboard listing.
    """
    model = MotherboardListing
    template_name = 'user_delete_templates/user_motherboardlisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'motherboard_listing'

    def test_func(self):
        motherboardlisting_object = self.get_object()
        return motherboardlisting_object.listing_seller == self.request.user


class CpuCoolerListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This class lets users delete their own CPU cooler listing.
    """
    model = CpuCoolerListing
    template_name = 'user_delete_templates/user_cpucoolerlisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'cpucooler_listing'

    def test_func(self):
        cpucoolerlisting_object = self.get_object()
        return cpucoolerlisting_object.listing_seller == self.request.user


class PcBuildListingByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    This class lets users delete their own PC build listing.
    """
    model = PcBuildListing
    template_name = 'user_delete_templates/user_pcbuildlisting_delete.html'
    success_url = '/pcportal/mylistings'
    context_object_name = 'pcbuildlisting'

    def test_func(self):
        pcbuildlisting_object = self.get_object()
        return pcbuildlisting_object.listing_seller == self.request.user


# Listing creation, update form views

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


class CpuListingByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    This class lets users update their own CPU listing.
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

    def test_func(self):
        cpulisting_object = self.get_object()
        return cpulisting_object.listing_seller == self.request.user


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


class PcBuildListingByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    This view lets users update their Pc build listings.
    """
    model = PcBuildListing
    form_class = UserPcbuildListingCreateForm
    template_name = 'user_create_templates/user_pcbuildlisting_form.html'
    success_url = '/pcportal/mylistings'

    def get_initial(self):
        prefill = super().get_initial()
        pcbuild_listing = self.get_object()
        pcbuild = pcbuild_listing.pc_build

        prefill['title'] = pcbuild.title
        prefill['cpu'] = pcbuild.cpu
        prefill['gpu'] = pcbuild.gpu
        prefill['psu'] = pcbuild.psu
        prefill['motherboard'] = pcbuild.motherboard
        prefill['cpucooler'] = pcbuild.cpucooler
        prefill['casepc'] = pcbuild.pc_case

        rambuild = RamBuild.objects.filter(pcbuild=pcbuild).first()
        if rambuild:
            prefill['ram'] = rambuild.ram
            prefill['ram_quantity'] = rambuild.quantity

        storagebuild = StorageBuild.objects.filter(pcbuild=pcbuild).first()
        if storagebuild:
            prefill['storage'] = storagebuild.storage
            prefill['storage_quantity'] = storagebuild.quantity

        return prefill

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

        pc_build = form.instance.pc_build
        pc_build.title = title
        pc_build.cpu = cpu
        pc_build.gpu = gpu
        pc_build.psu = psu
        pc_build.motherboard = motherboard
        pc_build.cpucooler = cpucooler
        pc_build.pc_case = casepc

        rambuild = RamBuild.objects.filter(pcbuild=pc_build)
        if rambuild:
            rambuild.ram = ram
            rambuild.quantity = ram_quantity
        else:
            RamBuild.objects.create(ram=ram, quantity=ram_quantity, pcbuild=pc_build)

        storagebuild = StorageBuild.objects.filter(pcbuild=pc_build)
        if storagebuild:
            storagebuild.storage = storage
            storagebuild.quantity = storage_quantity
        else:
            StorageBuild.objects.create(storage=storage, quantity=storage_quantity, pcbuild=pc_build)

        form.instance.pc_build = pc_build
        form.instance.price = price
        form.instance.listing_seller = self.request.user
        form.instance.seller = self.request.user.seller
        return super().form_valid(form)

    def test_func(self):
        pcbuildlisting_object = self.get_object()
        return pcbuildlisting_object.listing_seller == self.request.user


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


class GpuListingByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    This class lets users update their own GPU listing.
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

    def test_func(self):
        gpulisting_object = self.get_object()
        return gpulisting_object.listing_seller == self.request.user


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


class PsuListingByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    This class lets users update their own PSU listing.
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

    def test_func(self):
        psulisting_object = self.get_object()
        return psulisting_object.listing_seller == self.request.user


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


class RamListingByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    This class lets users update their own RAM listing.
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

    def test_func(self):
        ramlisting_object = self.get_object()
        return ramlisting_object.listing_seller == self.request.user


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


class StorageListingByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    This class lets users update their own Storage listing.
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

    def test_func(self):
        storagelisting_object = self.get_object()
        return storagelisting_object.listing_seller == self.request.user


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


class CasePCListingByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    This class lets users update their own PC case listing.
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

    def test_func(self):
        casepclisting_object = self.get_object()
        return casepclisting_object.listing_seller == self.request.user


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


class MotherboardListingByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    This class lets users update their own motherboard listing.
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

    def test_func(self):
        motherboardlisting_object = self.get_object()
        return motherboardlisting_object.listing_seller == self.request.user


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


class CpuCoolerListingByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    This class lets users update their own CPU cooler listing.
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

    def test_func(self):
        cpucoolerlisting_object = self.get_object()
        return cpucoolerlisting_object.listing_seller == self.request.user


# likes view
def like_pcbuildlistings(request, pcbuildlisting_id):
    """
    This function uses PC build listing's id to
    let the user like a specific PC build listing
    in a list page.
    """
    listing = get_object_or_404(PcBuildListing, id=pcbuildlisting_id)
    user_likes = UserLikes.objects.filter(user=request.user, pcbuild_listing=listing).first()
    if user_likes is None:
        UserLikes.objects.create(user=request.user, pcbuild_listing=listing)
    else:
        user_likes.delete()
    return redirect('pcbuild-listings')


def like_pcbuildlisting(request, pcbuildlisting_id):
    """
    This function uses PC build listing's id to
    let the user like a specific PC build listing
    in a pc build listing detail view.
    """
    listing = get_object_or_404(PcBuildListing, id=pcbuildlisting_id)
    user_likes = UserLikes.objects.filter(user=request.user, pcbuild_listing=listing).first()
    if user_likes is None:
        UserLikes.objects.create(user=request.user, pcbuild_listing=listing)
    else:
        user_likes.delete()
    return redirect('pcbuild-listing-one', pk=listing.id)
