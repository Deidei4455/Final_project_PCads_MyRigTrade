from django.shortcuts import render, redirect
from django.views import generic
from django.core.paginator import Paginator

from ..models.part_listing_models import (CpuListing, GpuListing, PsuListing,
                                          RamListing, StorageListing, CasePCListing,
                                          MotherboardListing, CpuCoolerListing)


# all part listings
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


# Individual part listings
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


# Part listings search view
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
