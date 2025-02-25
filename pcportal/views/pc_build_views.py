from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from django.db.models import Q

from ..models.build_with_listing import PcBuildListing, UserLikes


# PC build listing list view
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
        """
        This function checks if a user has liked
        the pc build listing, also check if a user
        is even logged in, without that the page would
        crash.
        """
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            for listing in context['pcbuildlistings']:
                listing.user_liked = listing.likes.filter(user=user).exists()
        return context


# PC build listing detail view
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
        """
        This function checks if a user has liked
        the pc build listing, also check if a user
        is even logged in, without that the page would
        crash.
        """
        context = super().get_context_data(**kwargs)
        user = self.request.user
        listing = context['pcbuildlisting']
        if user.is_authenticated:
            listing.user_liked = listing.likes.filter(user=user).exists()
        return context


# PC build search view
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


# likes view for PC build listings list
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


# likes view for PC build listing detail view
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
