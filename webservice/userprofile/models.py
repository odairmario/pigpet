from django.db import models
from django.contrib.auth.models import User
from utils import USER_TYPE_LIST
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE)
    # uid = models.CharField(max_length=20, null=False, blank=False)  # rut
    phone = models.CharField(max_length=20, null=True, blank=True)
    cell_phone = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    active = models.BooleanField(default=True)
    userType = models.CharField(choices=USER_TYPE_LIST, default='discente', max_length=100)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    # @receiver(post_save, sender=User)
    # def create_profile_for_user(sender, instance=None, created=False, **kargs):
    #     if created:
    #         UserProfile.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kargs):
        if instance:
            user_profile = UserProfile.objects.get(user=instance)
            user_profile.delete()