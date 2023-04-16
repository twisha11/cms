from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save


# Create your models here.
class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='img', blank=True, null=True, default='img/favicon.ico')
    about = models.TextField()
    profile_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.username
def create_profile(sender,instance,created, **kwargs):
    if created:
        user_profile = UserProfiles(user=instance)
        user_profile.username = instance
        user_profile.email = instance.email
        user_profile.username = instance.username
        user_profile.profession = ''
        user_profile.about = ''
        user_profile.save()
post_save.connect(create_profile, sender=User)