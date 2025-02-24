from django import forms

from .models import Profile, User, CpuListing


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class DateInput(forms.DateInput):
    input_type = 'date'



