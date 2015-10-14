import datetime
from django.db import models
from django import template
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import GroupedForeignKey
register = template.Library()

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)
    price = models.FloatField()
    old_price = models.FloatField()
    description = models.CharField(max_length=500)
    discount = models.IntegerField(blank=True)
    brand = models.CharField(max_length=200)
    catagory = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    item_number = models.IntegerField()
    link = models.CharField(max_length=500)
    product_id = models.IntegerField()
    def __str__(self):
        return self.item_name


class Blog(models.Model):
    name = models.CharField(max_length=200)
    auther = models.CharField(max_length=200)
    date = models.DateTimeField('Date Published')
    comments = models.IntegerField()
    hits = models.IntegerField()
    description = models.CharField(max_length=20000)
    count = models.IntegerField()
    order = models.IntegerField()
    filter_id = models.CharField(max_length=100)
    filter_no = models.IntegerField()
    def __str__(self):
        return self.name

class Subscribe_user(models.Model):
    mail = models.CharField(max_length=200)
    def __str__(self):
        return self.mail



class Catagory(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Sub_Catagory(models.Model):
    catagory = models.ForeignKey(Catagory)
    sub_name=models.CharField(max_length=200)
    def __str__(self):
        return self.sub_name

class Sub_Sub_Catagory(models.Model):
    sub_catagory = models.ForeignKey(Sub_Catagory)
    sub_sub_name=models.CharField(max_length=200)
    def __str__(self):
        return self.sub_sub_name        


class Item2(models.Model):
    catagory = models.ForeignKey(Catagory)
    item_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)
    price = models.FloatField()
    old_price = models.FloatField()
    description = models.CharField(max_length=500)
    discount = models.IntegerField(blank=True)
    item_number = models.IntegerField()
    product_id = models.IntegerField()
    def __str__(self):
        return self.item_name

class Item3(models.Model):
    catagory = models.ForeignKey(Catagory)
    sub_catagory = ChainedForeignKey(
        Sub_Catagory, 
        chained_field="catagory",
        chained_model_field="catagory", 
        show_all=False, 
        auto_choose=True
    )
    item_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)
    price = models.FloatField()
    old_price = models.FloatField()
    description = models.CharField(max_length=500)
    discount = models.IntegerField(blank=True)
    item_number = models.IntegerField()
    product_id = models.IntegerField()
    def __str__(self):
        return self.item_name




class Item4(models.Model):
    catagory = models.ForeignKey(Catagory)
    sub_catagory = ChainedForeignKey(
        Sub_Catagory, 
        chained_field="catagory",
        chained_model_field="catagory", 
        show_all=False, 
        auto_choose=True
    )
    sub_sub_catagory = ChainedForeignKey(
        Sub_Sub_Catagory, 
        chained_field="sub_catagory",
        chained_model_field="sub_catagory", 
        show_all=False, 
        auto_choose=True
    )
    item_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)
    price = models.FloatField()
    old_price = models.FloatField()
    description = models.CharField(max_length=500)
    discount = models.IntegerField(blank=True)
    item_number = models.IntegerField()
    product_id = models.IntegerField()
    def __str__(self):
        return self.item_name
