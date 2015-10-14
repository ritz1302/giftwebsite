from .forms import *
from .models import *
from carton.cart import Cart
from currencies.models import Currency
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import views, authenticate, login, update_session_auth_hash, update_session_auth_hash, logout as auth_logout
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.hashers import make_password
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
from hashlib import sha1 as sha_constructor
from itertools import chain
from operator import attrgetter
from paypal.standard.forms import PayPalPaymentsForm
import hashlib, datetime, random, paypalrestsdk, paypal
# Create your views here.




#index:

def index(request):
    list1 = Item2.objects.filter(catagory__name="teddy_bears")[:3]
    list2 = list1= Item2.objects.filter(catagory__name="teddy_bears").reverse()[:3]
    list3 = Item3.objects.filter(sub_catagory__catagory__name="flowers")
    list4 = Item3.objects.filter(sub_catagory__catagory__name="flowers")
    list5 = Item3.objects.filter(sub_catagory__catagory__name="cakes")
    list6 = Item.objects.filter(item_name = "icon")
    list7 = Item3.objects.filter(sub_catagory__catagory__name="cards")
    list8 = Item4.objects.filter(sub_sub_catagory__sub_catagory__catagory__name="cards")
    context = {'list1': list1, 'list2': list2, 'list3': list3, 'list4': list4,
               'list5': list5, 'list6': list6, 'list7': list7, 'list8': list8}
    return render(request, 'tohfa/index.html', context)




#login:

def login842d(request):
    return render(request, 'tohfa/login842d.html')

def login52ea(request):
    return render(request, 'tohfa/login52ea.html')

def login1234(request):
    return render(request, 'tohfa/login1234.html')

def loginfd9a(request):
    state = "Please click here to create an account."
    state1 = "If you have an account, Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state1 = "You're successfully logged in!"
            else:
                state1 = "Your account is not active, please contact the site admin."
        else:
            state1 = "Your username and/or password were incorrect."

    return render_to_response('tohfa/loginfd9a.html',
                              {'state':state, 'state1':state1, 'username': username},
                              context_instance=RequestContext(request))


def login546a(request):
    return render(request, 'tohfa/login546a.html')

def create_account(request):
    state1 = ""
    if request.POST:
        form = CreateAcount(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=request.POST['username'], 
                                                email=request.POST['email'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                password=request.POST['password'])

            #user_email = request.POST['email']
            #new_user.is_active()= False
            #send_mail(subject, message, from_email, to_list, fail_silently=True)
            #subject = 'Thank you for registration'
            #message = 'Welcome new user.\n here is the link to active your acount.
            #\nhttp://localhost:8000/shop/userlogin/'
            #from_email = settings.EMAIL_HOST_USER
            #to_list = [user_email, settings.EMAIL_HOST_USER]

            #send_mail(subject, message, from_email, to_list, fail_silently=True)
            state1 = "thanks for register, you may login now."
            return HttpResponseRedirect('/tohfa/login1')


    else:
        form = CreateAcount()

    args = {}
    args.update(csrf(request))

    args['form'] = form
    return render(request, 'tohfa/create_account.html', args)


#order:

def order(request):
    return render(request, 'tohfa/order.html')

def order815d(request):
    return render(request, 'tohfa/order815d.html')

def ordera5cc(request):
    return render(request, 'tohfa/ordera5cc.html')


#password recovery and search and subscribe:

def password_recovery(request):
    return render(request, 'tohfa/password-recovery.html')

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            items1 = Item2.objects.filter(item_name__icontains=q)
            items2= Item3.objects.filter(item_name__icontains=q)
            items3= Item4.objects.filter(item_name__icontains=q)
            items = chain(items1, items2, items3)
            return render(request, 'tohfa/search.html',
                {'items': items, 'query': q})
    return render(request, 'tohfa/search.html')

def subscr(request):
    state=""
    q=""
    if 'email' in request.POST:
        email = request.POST['email']
        
        if not email:
            error = True
        else:
            if not Subscribe_user.objects.filter(mail=email):
                q=Subscribe_user(mail=email)
                q.save()
                state="Thanks for subscription."
                return render(request, 'tohfa/subscr.html',
                              {'email':email, 'state':state})
            else:
                state="This email is already registered."
                return render(request, 'tohfa/subscr.html', {'state':state})
    return render(request, 'tohfa/subscr.html',{'state':state})


#blog:

def blog(request):
    return render(request, 'tohfa/blog.html')

def blogcd64(request):
    return render(request, 'tohfa/blogcd64.html')

def blog905b(request):
    return render(request, 'tohfa/blog905b.html')

def blogf80d(request):
    return render(request, 'tohfa/blogf80d.html')


#content

def about_us(request):
    return render(request, 'tohfa/4-about-us.html')

def delievery(request):
    return render(request, 'tohfa/1-delivery.html')

def legal_notice(request):
    return render(request, 'tohfa/2-legal-notice.html')

#blog:

def category1_c26(request):
    return render(request, 'tohfa/category-1-c26.html')

def sub_category1_c27(request):
    list1 = Blog.objects.filter(order = 1)[:5]
    context = {'list1': list1}
    return render(request, 'tohfa/sub-category-1-c27.html', context)

def sub_category2_c28(request):
    return render(request, 'tohfa/sub-category-2-c28.html')

def sub_category1_c27905b(request):
    list1 = Blog.objects.filter(order = 1).order_by('-count')[:2]
    context = {'list1': list1}
    return render(request, 'tohfa/sub-category-1-c27905b.html',context)


# dialog index

def dialog_index(request):
    return render(request, 'tohfa/dialog/index.html')

def default(request):
    return render(request, 'tohfa/module/productcomments/default.html')


#1234

def single(request, product_id):
    product1 = Item2.objects.filter(product_id=product_id)
    product2= Item3.objects.filter(product_id=product_id)
    product3= Item4.objects.filter(product_id=product_id)
    product = chain(product1, product2, product3)
    list1 = Item2.objects.all()[:4]
    list2 = Item3.objects.all()[:4]
    list3 = Item4.objects.all()[:4]
    list4 = Item4.objects.all().reverse()[:4]
    
    #sub_catagory = Sub_Catagory.objects.get(sub_sub_catagory=product.sub_sub_catagory)
    #catagory = Catagory.objects.get(sub_catagory__sub_name=sub_catagory)
    context = {'list1': list1, 'list2': list2, 'list3': list3,
               'list4': list4, 'product': product,}
    return render(request, 'tohfa/single.html', context)


def single2(request, count):
    product = get_object_or_404(Blog, count=count)
    list1 = Blog.objects.filter(order = 1)
    list2 = Blog.objects.filter(order= 2)
    context = {'product': product, 'list1': list1, 'list2': list2}
    return render(request, 'tohfa/single2.html', context)

def blog1234(request, filter_no):
    list1 = Blog.objects.filter(filter_no=filter_no)
    state= list1[0].filter_id
    context = {'list1': list1, 'state': state}
    return render(request, 'tohfa/blog1234.html', context)


def catagory(request, catagory):
    if catagory == "teddy_bears":
        list1= Item2.objects.filter(catagory__name=catagory)
    elif catagory == "cards":
        list1= Item4.objects.filter(sub_sub_catagory__sub_catagory__catagory__name=catagory)
        list11= Item3.objects.filter(sub_catagory__catagory__name=catagory)
        list1 = chain(list1, list11)
    else:
        list1= Item3.objects.filter(sub_catagory__catagory__name=catagory)
    list2=Sub_Catagory.objects.filter(catagory__name=catagory)
    list3=Sub_Sub_Catagory.objects.all()
    state = False
    list4 = Sub_Sub_Catagory.objects.values_list('sub_catagory', flat= True).distinct()
    context = {'list1': list1, 'list2':list2, 'list3':list3,
                   'list4':list4, 'catagory':catagory, 'state':state}
    return render(request, 'tohfa/catagory.html', context)
    
    


def sub_catagory(request, sub_catagory):
    catagory = Catagory.objects.get(sub_catagory__sub_name=sub_catagory)
    list1= Sub_Sub_Catagory.objects.filter(sub_catagory__sub_name=sub_catagory)
    if sub_catagory =="relations":
        list2= Item4.objects.filter(sub_sub_catagory__sub_catagory__sub_name=sub_catagory)
    elif sub_catagory == "ocassions":
        list2= Item4.objects.filter(sub_sub_catagory__sub_catagory__sub_name=sub_catagory)
    else:
        list2= Item3.objects.filter(sub_catagory__sub_name=sub_catagory)
        
    context = {'sub_catagory':sub_catagory, 'list1':list1, 'catagory':catagory, 'list2':list2}
    return render(request, 'tohfa/sub_catagory.html', context )

def sub_sub_catagory(request, sub_sub_catagory):
    sub_catagory = Sub_Catagory.objects.get(sub_sub_catagory__sub_sub_name=sub_sub_catagory)
    catagory = Catagory.objects.get(sub_catagory__sub_name=sub_catagory)
    list1= Item4.objects.filter(sub_sub_catagory__sub_sub_name=sub_sub_catagory)
    list2= Item4.objects.filter(sub_sub_catagory__sub_sub_name=sub_sub_catagory)
    context = {'catagory':catagory, 'list2':list2,
               'sub_sub_catagory':sub_sub_catagory, 'list1':list1, 'sub_catagory':sub_catagory}
    return render(request, 'tohfa/sub_sub_catagory.html', context)



def add(request, product_id):
    cart = Cart(request.session)
    if Item2.objects.filter(product_id=product_id):
        product = Item2.objects.get(product_id=product_id)
    elif Item3.objects.filter(product_id=product_id):
        product = Item3.objects.get(product_id=product_id)
    else:
        product = Item4.objects.get(product_id=product_id)
    
    cart.add(product, price=product.price)
    return HttpResponseRedirect('/tohfa/show')


def show(request):
    state=""
    currency_in = 'INR'
    currency_out = 'USD'
    import urllib.request
    req = urllib.request.urlopen('http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s='+currency_in+currency_out+'=X')
    rrr = req.read()
    state1= rrr.decode('utf-8')
    state2= state1.split(',')
    state=state2[1]
    return render(request, 'tohfa/show_cart.html', {'state': state,'paypal_url': settings.PAYPAL_URL,
                                                   'paypal_email': settings.PAYPAL_EMAIL,
                                                   'paypal_return_url': settings.PAYPAL_RETURN_URL  })



def remove(request, product_id):
    cart = Cart(request.session)
    if Item2.objects.filter(product_id=product_id):
        product = Item2.objects.get(product_id=product_id)
    elif Item3.objects.filter(product_id=product_id):
        product = Item3.objects.get(product_id=product_id)
    else:
        product = Item4.objects.get(product_id=product_id)
    cart.remove(product)
    return HttpResponseRedirect('/tohfa/show')

def remove_single(request, product_id):
    cart = Cart(request.session)
    if Item2.objects.filter(product_id=product_id):
        product = Item2.objects.get(product_id=product_id)
    elif Item3.objects.filter(product_id=product_id):
        product = Item3.objects.get(product_id=product_id)
    else:
        product = Item4.objects.get(product_id=product_id)
    cart.remove_single(product)
    return HttpResponseRedirect('/tohfa/show')

def empty(request):
    cart= Cart(request.session)
    cart.clear()
    return HttpResponseRedirect('/tohfa/')



def thankyou(request):
    return render(request, 'shop/thankyou.html')
