from django.urls import path
from . import views

urlpatterns = [
    # main
    path('', views.index, name='index_n'),

    # user profile
    path('register/', views.register_user, name='register'),
    path('profile/', views.get_user_profile, name='user-profile'),

    # sellers
    path('sellers/', views.SellerListView.as_view(), name='sellers-all'),
    path('sellers/<int:pk>', views.SellerDetailView.as_view(), name='seller-one'),

    # user listings
    path('mylistings/', views.get_user_listings, name='my-listings'),
    # seller listings
    path('sellers/<int:seller_id>/pcbuildlistings/', views.get_seller_listings, name='seller-listings'),

    # all listings
    path('partlistings/', views.get_part_listings, name='part-listings'),
    path('pcbuildlistings/', views.PcBuildListingListView.as_view(), name='pcbuild-listings'),

    # all parts list
    path('parts/', views.get_all_parts, name='part-list'),

    # individual listings
    path('pcbuildlistings/<int:pk>', views.PcBuildListingDetailView.as_view(), name='pcbuild-listing-one'),
    path('partlistings/cpu/<int:pk>', views.CpuListingDetailView.as_view(), name='cpu-listing-one'),
    path('partlistings/gpu/<int:pk>', views.GpuListingDetailView.as_view(), name='gpu-listing-one'),
    path('partlistings/psu/<int:pk>', views.PsuListingDetailView.as_view(), name='psu-listing-one'),
    path('partlistings/ram/<int:pk>', views.RamListingDetailView.as_view(), name='ram-listing-one'),
    path('partlistings/storage/<int:pk>',
         views.StorageListingDetailView.as_view(), name='storage-listing-one'),
    path('partlistings/casepc/<int:pk>',
         views.CasePCListingDetailView.as_view(), name='casepc-listing-one'),
    path('partlistings/motherboard/<int:pk>',
         views.MotherboardListingDetailView.as_view(), name='motherboard-listing-one'),
    path('partlistings/cpucooler/<int:pk>',
         views.CpuCoolerListingDetailView.as_view(), name='cpucooler-listing-one'),

    # search
    path('sellers/search/', views.search_seller, name='search-seller'),
    path('partlistings/search/', views.search_part_listings_by_price, name='search-partlistings'),
    path('pcbuildlistings/search/', views.search_pcbuildlisting, name='search-pcbuildlisting'),

    # delete
    path('mylistings/cpu/delete/<int:pk>', views.CpuListingByUserDeleteView.as_view(),
         name='user-delete-cpulisting'),
    path('mylistings/gpu/delete/<int:pk>', views.GpuListingByUserDeleteView.as_view(),
         name='user-delete-gpulisting'),
    path('mylistings/psu/delete/<int:pk>', views.PsuListingByUserDeleteView.as_view(),
         name='user-delete-psulisting'),
    path('mylistings/ram/delete/<int:pk>', views.RamListingByUserDeleteView.as_view(),
         name='user-delete-ramlisting'),
    path('mylistings/storage/delete/<int:pk>', views.StorageListingByUserDeleteView.as_view(),
         name='user-delete-storagelisting'),
    path('mylistings/casepc/delete/<int:pk>', views.CasePCListingByUserDeleteView.as_view(),
         name='user-delete-casepclisting'),
    path('mylistings/motherboard/delete/<int:pk>', views.MotherboardListingByUserDeleteView.as_view(),
         name='user-delete-motherboardlisting'),
    path('mylistings/cpucooler/delete/<int:pk>', views.CpuCoolerListingByUserDeleteView.as_view(),
         name='user-delete-cpucoolerlisting'),
    path('mylistings/pcbuildlisting/delete/<int:pk>', views.PcBuildListingByUserDeleteView.as_view(),
         name='user-delete-pcbuildlisting'),

    # update listings
    path('mylistings/cpu/update/<int:pk>', views.CpuListingByUserUpdateView.as_view(),
         name='user-update-cpulisting'),
    path('mylistings/gpu/update/<int:pk>', views.GpuListingByUserUpdateView.as_view(),
         name='user-update-gpulisting'),
    path('mylistings/psu/update/<int:pk>', views.PsuListingByUserUpdateView.as_view(),
         name='user-update-psulisting'),
    path('mylistings/ram/update/<int:pk>', views.RamListingByUserUpdateView.as_view(),
         name='user-update-ramlisting'),
    path('mylistings/storage/update/<int:pk>', views.StorageListingByUserUpdateView.as_view(),
         name='user-update-storagelisting'),
    path('mylistings/casepc/update/<int:pk>', views.CasePCListingByUserUpdateView.as_view(),
         name='user-update-casepclisting'),
    path('mylistings/motherboard/update/<int:pk>', views.MotherboardListingByUserUpdateView.as_view(),
         name='user-update-motherboardlisting'),
    path('mylistings/cpucooler/update/<int:pk>', views.CpuCoolerListingByUserUpdateView.as_view(),
         name='user-update-cpucoolerlisting'),
    path('mylistings/pcbuildlisting/<int:pk>', views.PcBuildListingByUserUpdateView.as_view(),
         name='user-update-pcbuildlisting'),

    # create listings
    path('createlistings/cpulisting/', views.CpuListingByUserCreateView.as_view(),
         name='create-cpulisting'),
    path('createlistings/gpulisting/', views.GpuListingByUserCreateView.as_view(),
         name='create-gpulisting'),
    path('createlistings/psulisting/', views.PsuListingByUserCreateView.as_view(),
         name='create-psulisting'),
    path('createlistings/ramlisting/', views.RamListingByUserCreateView.as_view(),
         name='create-ramlisting'),
    path('createlistings/storagelisting/', views.StorageListingByUserCreateView.as_view(),
         name='create-storagelisting'),
    path('createlistings/casepclisting/', views.CasePCListingByUserCreateView.as_view(),
         name='create-casepclisting'),
    path('createlistings/motherboardlisting/', views.MotherboardListingByUserCreateView.as_view(),
         name='create-motherboardlisting'),
    path('createlistings/cpucoolerlisting/', views.CpuCoolerListingByUserCreateView.as_view(),
         name='create-cpucoolerlisting'),
    path('createlistings/pcbuildlisting/', views.PcBuildListingByUserCreateView.as_view(),
         name='create-pcbuildlisting'),

    # liking PC build listings
    path('likepcbuildlistings/<int:pcbuildlisting_id>', views.like_pcbuildlistings,
         name='like-pcbuildlistings'),
    path('likepcbuildlisting/<int:pcbuildlisting_id>', views.like_pcbuildlisting,
         name='like-pcbuildlisting'),
]
