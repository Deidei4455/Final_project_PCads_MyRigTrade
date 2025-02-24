from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, User, Seller


@receiver(post_save, sender=User)
def create_profile_and_seller(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
