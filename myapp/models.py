from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("index")


class Image(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete = models.SET_NULL)
    image = models.ImageField(upload_to='images')
    cat = models.ForeignKey(Category,on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")
    

    def get_absolute_url(self):
        return reverse("index")
    


LIKES_CHOICES = (
    ('Like','Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete = models.SET_NULL)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    value = models.CharField(choices = LIKES_CHOICES , default='Like', max_length=10)

    def __str__(self):
        return self.value
    