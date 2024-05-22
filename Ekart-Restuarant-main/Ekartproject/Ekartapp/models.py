from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return  reverse('Ekartapp:Products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


<<<<<<< HEAD



# class Product(models.Model):
#     PACKET_CHOICES = [
#         ('Pillow Pouch', 'Pillow Pouch'),
#         ('Standup Pouch', 'Standup Pouch'),
#         ('Pouch', 'Pouch'),
#         ('Bottle', 'Bottle'),
#         ('Box', 'Box'),
#     ]
#
#     GRAMS_CHOICES = [
#         (20, '20g'),
#         (60, '60g'),
#         (130, '130g'),
#         (150, '150g'),
#         (300, '300g'),
#         (400, '400g'),
#     ]
#
#     name = models.CharField(max_length=250, unique=True)
#     slug = models.SlugField(max_length=250, unique=True)
#     description = models.TextField(blank=True)
#
#     packet = models.CharField(max_length=20, choices=PACKET_CHOICES)
#     grams = models.IntegerField(choices=GRAMS_CHOICES)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#
#
#
=======
# class Product(models.Model):
#     name = models.CharField(max_length=250, unique=True)
#     slug = models.SlugField(max_length=250, unique=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
>>>>>>> d4c4eead28b5a93d352fb1a0951df745ce6bed89
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product', blank=True)
#     stock = models.IntegerField()
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#
#     def get_url(self):
#         return  reverse('Ekartapp:proCatdetail',args=[self.category.slug,self.slug])
#
#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'product'
#         verbose_name_plural = 'products'
#
#     def __str__(self):
#         return '{}'.format(self.name)
<<<<<<< HEAD
=======
#


>>>>>>> d4c4eead28b5a93d352fb1a0951df745ce6bed89
class Product(models.Model):
    PACKET_CHOICES = [
        ('Pillow Pouch', 'Pillow Pouch'),
        ('Standup Pouch', 'Standup Pouch'),
        ('Pouch', 'Pouch'),
        ('Bottle', 'Bottle'),
        ('Box', 'Box'),
    ]

    GRAMS_CHOICES = [
        (20, '20g'),
        (60, '60g'),
        (130, '130g'),
        (150, '150g'),
        (300, '300g'),
        (400, '400g'),
    ]

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
<<<<<<< HEAD
    packet = models.CharField(max_length=20, choices=PACKET_CHOICES)
    grams = models.IntegerField(choices=GRAMS_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='product', blank=True)
    image2 = models.ImageField(upload_to='product', blank=True)
    image3 = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
=======
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    # stock = models.IntegerField()
>>>>>>> d4c4eead28b5a93d352fb1a0951df745ce6bed89
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('Ekartapp:proCatdetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
<<<<<<< HEAD
        return '{}'.format(self.name)
=======
        return '{}'.format(self.name)

class PacketSize(models.Model):
    PACKET_CHOICES = [
        ('Pillow Pouch', 'Pillow Pouch'),
        ('Standup Pouch', 'Standup Pouch'),
        ('Pouch', 'Pouch'),
        ('Bottle', 'Bottle'),
        ('Box', 'Box'),
    ]

    GRAMS_CHOICES = [
        (20, '20g'),
        (60, '60g'),
        (130, '130g'),
        (150, '150g'),
        (300, '300g'),
        (400, '400g'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    packet = models.CharField(max_length=20, choices=PACKET_CHOICES)
    grams = models.IntegerField(choices=GRAMS_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product', blank=True)

    class Meta:
        verbose_name = 'packet size'
        verbose_name_plural = 'packet sizes'

    def __str__(self):
        return f"{self.product.name} - {self.packet} - {self.grams}g - ${self.price} - Stock: {self.stock}"


>>>>>>> d4c4eead28b5a93d352fb1a0951df745ce6bed89
