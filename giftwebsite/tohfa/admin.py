from django.contrib import admin
from .models import *
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['item_name']}),
        ('product id',        {'fields': ['product_id']}),
        ('item number',      {'fields': ['item_number']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('old_price',         {'fields': ['old_price']}),
        ('price',             {'fields': ['price']}),
        ('description',        {'fields': ['description']}),
        ('image1',            {'fields': ['image1']}),
        ('image2',            {'fields': ['image2']}),
        ('image3',            {'fields': ['image3']}),
        ('image4',            {'fields': ['image4']}),
        ('image5',            {'fields': ['image5']}),
        ('image6',            {'fields': ['image6']}),
        ('discount',          {'fields': ['discount']}),
        ('catagory',           {'fields': ['catagory']}),
        ('brand',             {'fields': ['brand']}),
        ('color',             {'fields': ['color']}),
        ('link',              {'fields': ['link']}),
    ]
    list_display = ('item_name', 'product_id', 'item_number', 'pub_date', 'old_price', 'price', 'discount', 'catagory', 'link', 'brand', 'color', 'description', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6',)
    list_filter = ['pub_date']
    search_fields = ['item_name']
    ordering = ('product_id',)



    
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Auther',           {'fields': ['auther']}),
        ('Count',            {'fields': ['count']}),
        ('Order',            {'fields': ['order']}),
        ('Filter Id',        {'fields': ['filter_id']}),
        ('Filter No',        {'fields': ['filter_no']}),
        ('Date',             {'fields': ['date']}),
        ('Description',      {'fields': ['description']}),
        ('Comments',         {'fields': ['comments']}),
        ('Hits',             {'fields': ['hits']}),
    ]
    list_display = ('name', 'auther', 'count', 'order', 'filter_id', 'filter_no', 'date', 'comments', 'hits',)
    list_filter = ['date']
    search_fields = ['name']
    ordering = ('name',)
    #list_editable = ('filter_no', 'hits')

class Subscribe_userAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User Email',             {'fields': ['mail']}),
    ]
    list_display = ('mail',)




class Sub_Sub_CatagoryInline(admin.StackedInline):
    model = Sub_Sub_Catagory
    extra = 3
    
class Sub_CatagoryInline(admin.StackedInline):
    model = Sub_Catagory
    extra = 3

    
class CatagoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name',              {'fields': ['name']}),
    ]
    list_display = ('name', 'id')
    inlines = [Sub_CatagoryInline]

class Sub_CatagoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('catagory',              {'fields': ['catagory']}),
        ('sub name',              {'fields': ['sub_name']}),
    ]
    list_display = ('sub_name', 'id', 'catagory')
    inlines = [Sub_Sub_CatagoryInline]

    
class Sub_Sub_CatagoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('sub_catagory',              {'fields': ['sub_catagory']}),
        ('sub sub name',              {'fields': ['sub_sub_name']}),
    ]
    list_display = ('sub_sub_name', 'id', 'sub_catagory')

admin.site.register(Item2)
admin.site.register(Item3)    
admin.site.register(Item4)    
admin.site.register(Catagory, CatagoryAdmin)    
admin.site.register(Sub_Catagory, Sub_CatagoryAdmin)    
admin.site.register(Sub_Sub_Catagory, Sub_Sub_CatagoryAdmin)    
admin.site.register(Item, ItemAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Subscribe_user,Subscribe_userAdmin)
