from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic

from django.db.models import Q

from ..models.seller_model import Seller

from ..models.part_listing_models import (CpuListing, GpuListing, PsuListing,
                                          RamListing, StorageListing, CasePCListing,
                                          MotherboardListing, CpuCoolerListing)

from ..models.build_with_listing import PcBuildListing

from ..forms import SellerReviewForm


# Sellers list view
class SellerListView(generic.ListView):
    """
    This class retrieves a list of all sellers
    and renders them in all sellers list page.
    """
    model = Seller
    context_object_name = "sellers_list"
    template_name = "sellers.html"
    paginate_by = 6


# One seller detail view with review option
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


# seller search results view
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


# Seller's listings view
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
