from django.db import models


# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=20,verbose_name='نام کاربری')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    birthday = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}--{self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img = models.ImageField(upload_to='product_img', null=True, blank=True)

    def __str__(self):
        return self.name


class OrderApp(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.IntegerField()
    counter = models.PositiveIntegerField()
    price_all = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.first_name + '-' + self.customer.last_name + '-' + self.product.name
