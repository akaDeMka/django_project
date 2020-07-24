from .models import Profile
from django.contrib.auth.models import Group

def create_profile(sender, instance, created, **kwargs):
    obj, created = Profile.objects.get_or_create(
        user=instance,
        defaults={},
    )
    if created:
        obj, created = Group.objects.get_or_create(
        name='Customer',
        defaults={},
        )
        my_group = Group.objects.get(name='Customer')
        my_group.user_set.add(instance)
