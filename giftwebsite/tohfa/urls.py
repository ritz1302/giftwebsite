from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<catagory>.+?)/catagory$', views.catagory, name='catagory'),
    url(r'^(?P<sub_catagory>.+?)/sub_catagory$', views.sub_catagory, name='sub_catagory'),
    url(r'^(?P<sub_sub_catagory>.+?)/sub_sub_catagory$', views.sub_sub_catagory, name='sub_sub_catagory'),
    url(r'^(?P<product_id>[0-9]+)/single$', views.single, name='single'),
    url(r'^(?P<count>[0-9]+)/single2$', views.single2, name='single2'),
    url(r'^(?P<filter_no>[0-9]+)/blog1234$', views.blog1234, name='blog1234'),
    url(r'^category1_c26/$', views.category1_c26, name='category1_c26'),
    url(r'^sub_category1_c27/$', views.sub_category1_c27, name='sub_category1_c27'),
    url(r'^sub_category2_c28/$', views.sub_category2_c28, name='sub_category2_c28'),
    url(r'^sub_category1_c27905b/$', views.sub_category1_c27905b, name='sub_category1_c27905b'),
    url(r'^order8/$', views.order815d, name='order815d'),
    url(r'^order16/$', views.ordera5cc, name='ordera5cc'),
    url(r'^order21/$', views.order, name='order'),
    url(r'^password_recovery/$', views.password_recovery, name='password_recovery'),
    url(r'^search/$', views.search, name='search'),
    url(r'^subscr/$', views.subscr, name='subscr'),
    url(r'^login2/$', views.login1234, name='login1234'),
    url(r'^login15/$', views.login842d, name='login842d'),
    url(r'^login9/$', views.login52ea, name='login52ea'),
    url(r'^login1/$', views.loginfd9a, name='loginfd9a'),
    url(r'^login14/$', views.login546a, name='login546a'),
    url(r'^create_account/$', views.create_account, name='create_account'),
    url(r'^blog2/$', views.blog, name='blog'),
    url(r'^blog7/$', views.blog905b, name='blog905b'),
    url(r'^blog10/$', views.blogcd64, name='blogcd64'),
    url(r'^blog12/$', views.blogf80d, name='blogf80d'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^delievery/$', views.delievery, name='delievery'),
    url(r'^legal_notice/$', views.legal_notice, name='legal_notice'),
    url(r'^dialog_index/$', views.dialog_index, name='dialog_index'),
    url(r'^default/$', views.default, name='default'),
    url(r'^(?P<product_id>[0-9]+)/add/$', views.add, name='add'),
    url(r'^show/$', views.show, name='show'),
    url(r'^(?P<product_id>[0-9]+)/remove/$', views.remove, name='remove'),
    url(r'^empty/$', views.empty, name='empty'),
    url(r'^thankyou/$', views.thankyou, name='thankyou'),
    url(r'^(?P<product_id>[0-9]+)/remove_single/$', views.remove_single, name='remove_single'),

       
]   
