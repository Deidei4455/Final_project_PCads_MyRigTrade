from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from ..models.part_listing_models import (CpuListing, GpuListing, PsuListing,
                                          RamListing, StorageListing, CasePCListing,
                                          MotherboardListing, CpuCoolerListing)

from ..models.build_with_listing import PcBuildListing


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
