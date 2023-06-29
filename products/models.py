from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    manufacturer = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    condition = models.CharField(max_length=255)
    description = models.TextField(null=True)
    features = models.TextField()
    dimensions = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='caravan_images/', blank=True, null=True)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brand_logos/', blank=True, null=True)

    def __str__(self):
        return self.name


class SliderImage(models.Model):
    image = models.ImageField(upload_to='slider_images/')

    def __str__(self):
        return self.image.name


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
