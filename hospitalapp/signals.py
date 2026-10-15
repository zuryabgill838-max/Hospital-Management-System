from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(
            user=instance
        )

        # Default group for new normal users
        if not instance.is_superuser:
            group = Group.objects.filter(
                name="Receptionist"
            ).first()

            if group:
                instance.groups.add(group)