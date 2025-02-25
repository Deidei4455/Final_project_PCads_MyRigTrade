from django.shortcuts import render, redirect

from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from ..models.seller_model import Seller

from ..models.part_listing_models import (CpuListing, GpuListing, PsuListing,
                                          RamListing, StorageListing, CasePCListing,
                                          MotherboardListing, CpuCoolerListing)

from ..models.build_with_listing import PcBuildListing

from ..forms import ProfileUpdateForm, UserUpdateForm, User

from ..utils import check_password


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
