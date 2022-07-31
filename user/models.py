from django.db import models
from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20) 

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    image= models.ImageField(upload_to='media/products/')

    @staticmethod
    def get_all_products(): 
        return Product.objects.all()

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)