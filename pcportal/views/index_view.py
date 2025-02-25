from django.shortcuts import render

from ..models.seller_model import Seller

from ..models.part_models import Cpu, Gpu, Psu, Ram, Storage, CasePC, Motherboard, CpuCooler

from ..models.part_listing_models import (CpuListing, GpuListing, PsuListing,
                                          RamListing, StorageListing, CasePCListing,
                                          MotherboardListing, CpuCoolerListing)

from ..models.build_with_listing import PcBuild, PcBuildListing


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
