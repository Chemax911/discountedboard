from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from src.dashboard.models import Profile

User = get_user_model()


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
