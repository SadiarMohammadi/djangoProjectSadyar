from django.db import models


# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=20, verbose_name='نام کاربری')
    first_name = models.CharField(max_length=25, verbose_name='نام ')
    last_name = models.CharField(max_length=30, verbose_name='نام خانوادگی')
    mobile = models.CharField(max_length=11, verbose_name='موبایل')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    birthday = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ تولد')

    def __str__(self):
        return f'{self.first_name}--{self.last_name}'

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'


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
