from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    catimage = models.ImageField(upload_to='catphotos')
    def __str__(self):
        return self.title
    


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    added_date = models.DateTimeField()
    cat = models.ForeignKey(Category,on_delete = models.CASCADE)


    def __str__(self):
        return self.title
    