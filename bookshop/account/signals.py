from .models import Profile
from django.contrib.auth.models import Group

def create_profile(sender, instance, created, **kwargs):
    obj, created = Profile.objects.get_or_create(
        user=instance,
        defaults={},
    )
    if created:
        try:
            my_group = Group.objects.get(name='Customer')
        except:
            my_group = Group.objects.create(name='Customer')
        my_group.user_set.add(instance)
