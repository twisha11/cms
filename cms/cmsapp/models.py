from django.db import models
import uuid
from ckeditor.fields import RichTextField
from profiles.models import UserProfiles


# Create your models here.
class Post(models.Model):
    writer = models.ForeignKey(UserProfiles, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='img')
    body = RichTextField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default=uuid.uuid4)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    commenter = models.CharField(max_length=50)
    body = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return self.body


