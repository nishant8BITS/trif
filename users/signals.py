from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# When user is saved, send a signal to this function, passing the user,
# so a profile is created for the user

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# Following not testing ok, needs tweaking...
# def save_profile(sender, instance, **kwargs):
#     img = resizeimage.resize_height(instance.profile.image, 128)
#     instance.profile.image = img
#     instance.profile.save(self, **kwargs)