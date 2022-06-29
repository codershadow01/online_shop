from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    category_image=models.ImageField(upload_to="category/", default="category/default2.jpg")
    slugc=models.SlugField(default="", blank=True)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("category", args=[self.slugc] )
    
    def save(self, *args, **kwargs):
        self.slugc=slugify(self.category_name)
        return super().save(*args,**kwargs)

    class Meta:
        verbose_name_plural="Categories"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    item_cost = models.DecimalField(decimal_places=2, max_digits=20)
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(default="")
    image = models.ImageField(upload_to="shop/", default="shop/default1.jpg", height_field="image_height", width_field="image_width")
    image_height = models.IntegerField(default=10)
    image_width = models.IntegerField(default=10)
    slug = models.SlugField(default="", blank=True)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.item_name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product", kwargs={"category": self.category.slugc, "slug": self.slug})

    def __str__(self):
        return self.item_name + " " + (self.category.category_name)

class Staff(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    area = models.TextField()
    about = models.TextField()
    item_delivery = models.ForeignKey(Product, models.SET_NULL, blank=True, null=True,)

    def __str__(self):
        return self.name + " " + self.area

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.IntegerField(null=False)

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)