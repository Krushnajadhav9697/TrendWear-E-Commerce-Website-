from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from products.models import Product,Category
from cart.models import Cart
from .models import Profile
from payment.models import OrderItem
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from payment.models import Order
import paypalrestsdk
from django.conf import settings

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # sandbox or live
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

# from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
        return render(request,'index.html')


def register_view(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password1']
        confirm_pass=request.POST['password2']
        if pass1!=confirm_pass:
            messages.warning(request,'password is not matching')
            return render(request,'register.html')
        try:
            if User.objects.get(username=username):
                messages.info(request,'Email is Taken')
                return render(request,'register.html')
                
        except Exception as identifier:
            pass 
        user=User.objects.create_user(username,username,pass1)
        user.save()
        messages.info(request,"User Creatd! Log-in for more!")
        return redirect('/login')
    return render(request,'register.html')

  
    

def login_view(request):
    if request.method=='POST':
        uname=request.POST['username']
        upassw=request.POST.get('password')
        user=authenticate(username=uname,password=upassw)
        if user is not None:
            login(request,user)
            messages.error(request,'Log-in Successful')
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def logout_view(request):
    logout(request)
    messages.info(request,'Logout Success')
    return redirect('/login')

def customer_servivce(request):
    return render(request,'customer_service.html')
    
        
@login_required(login_url='/login')  
def myprofile(request):
   
    user_profile = Profile.objects.filter(user=request.user).first()

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin_code = request.POST.get('pin_code')

        if user_profile:
            
            user_profile.full_name = full_name
            user_profile.email = email
            user_profile.phone = phone
            user_profile.street = street
            user_profile.city = city
            user_profile.state = state
            user_profile.pin_code = pin_code
            user_profile.save()
            messages.info(request, 'Your profile has been updated.')
            return redirect('/')
        else:
           
            user_profile = Profile.objects.create(
                user=request.user,
                full_name=full_name,
                email=email,
                phone=phone,
                street=street,
                city=city,
                state=state,
                pin_code=pin_code
            )
            messages.info(request, 'Your profile has been created.')
            return redirect('/')

 
    return render(request, 'myprofile.html', {'profile': user_profile})
        

def women_p_list(request):
    wl=Product.objects.all()
    context={'wl':wl}
    return render(request,'women_p_list.html',context)

def men_list(request):
    # ml=Product.objects.filter(gender=gender)
    # context={'ml':ml}
    return render(request,'men.html')

def tops_view(request):
    wl=Product.objects.all()
    context={'wl':wl}
    return render (request,'wcategorywise.html',context)



@login_required(login_url='/login')
def add_to_cart(request, pid):
    product = get_object_or_404(Product, id=pid)
    user = request.user
    if Cart.objects.filter(user=user, product=product).exists():
        messages.info(request,'Product Already in In Cart,You can increase the quantity in cart list ')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        # return redirect('/womenlist')

    c = Cart()
    c.product = product
    c.user = user
    c.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    # return redirect('/')

    
# def cart_list(request):
#     uid=request.session.get('uid')
#     # user_id=User.objects.get(id=uid)
#     # print(user_id)
#     cl=Cart.objects.filter(user_id=uid)
#     context={'cl':cl}
#     print(cl)
#     return render(request,'cart.html',context)

def cart_list(request):
    cl = Cart.objects.filter(user=request.user)  
    context = {'cl': cl}
    
    return render(request, 'cart.html', context)


    
class delete_cart(DeleteView):
    template_name='delete.html'
    model=Cart
    success_url='/clist'

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    id = Product.objects.all()

    return render(request, 'wcategorywise.html', {
        'category': category,
        'products': products
    })

def product_search(request):
    uid=request.session.get('uid')
    srch=request.POST.get('srch')
    wl=Product.objects.filter(name__contains=srch)
    context={'wl':wl ,'srch':srch}
    return render(request,'search_result.html',context)

# def product_search(request):
#     uid = request.session.get('uid')
#     srch = request.POST.get('srch')
#     category = request.POST.get('category')  # Add this to capture category from the form

#     # Filter products by search query and category
#     if srch:
#         if category == 'Women':
#             wl = Product.objects.filter(name__icontains=srch, gender='Women')
#         elif category == 'Men':
#             wl = Product.objects.filter(name__icontains=srch, gender='Men')
#         elif category == 'baby':
#             wl = Product.objects.filter(name__icontains=srch, gender='baby')
#         elif category == 'kids':
#             wl = Product.objects.filter(name__icontains=srch, gender='kids')
#         elif category == 'sports':  
#             wl = Product.objects.filter(name__icontains=srch, gender='sports')
#         # Add additional filters for other categories if needed (e.g., Kids, Baby, etc.)
#         else:
#             wl = Product.objects.filter(name__icontains=srch)  # General search without category
#     else:
#         wl = Product.objects.none()

#     context = {'wl': wl, 'srch': srch}
#     return render(request, 'search_result.html', context)


def gen_list(request):
    uid=request.session.get('uid')
    genl=Product.objects.all()
    gent=set()
    for i in genl:  
        gent.add(i.gender)
    print(gent)
    context={'genl':genl,'gent':gent}
    return render(request,'sort.html',context)


def product_list_view(request):
    section_choices = dict(Product.SECTION_CHOICES)
    products = Product.objects.all()
    context = {
        'section_choices': section_choices,
        'products': products
    }

    return render(request, 'pro_list.html', context)



def section_view(request, section):
    products = Product.objects.filter(gender=section)
    section_choices = dict(Product.SECTION_CHOICES)
    print(section_choices)
    context = {
        'products': products,
        'section': section,  
    }

    if section == 'Men':
        return render(request, 'men.html', context)
    elif section == 'Women':
        return render(request, 'women.html', context)
    elif section == 'Kids':
        return render(request, 'kids.html', context)
    elif section == 'Baby':
        return render(request, 'baby.html', context)
    elif section == 'Sports':
        return render(request, 'sport.html', context)
    else:
        return render(request, 'index.html', context)


# def checkout(request):
#     profile = Profile.objects.get(user=request.user)
#     delivery_address = {
#         'street': profile.street or '',
#         'city': profile.city or '',
#         'state': profile.state or '',
#         'pin_code': profile.pin_code or ''
#     }

#     if request.method == 'POST':
      
#         street = request.POST.get('street')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         pin_code = request.POST.get('pin_code')
        
       
#         total_price = 0.00  
        
#         order = Order.objects.create(
#             user=request.user,
#             full_name=profile.full_name,
#             email=profile.email,
#             phone=profile.phone,
#             delivery_street=street,
#             delivery_city=city,
#             delivery_state=state,
#             delivery_pin_code=pin_code,
#             total_price=total_price
#         )
#         order.save()
        
#         return redirect('order_success')  

#     return render(request, 'checkout.html', {'profile': profile, 'delivery_address': delivery_address})


def checkout(request):
    profile = Profile.objects.get(user=request.user)
    delivery_address = {
        'street': profile.street or '',
        'city': profile.city or '',
        'state': profile.state or '',
        'pin_code': profile.pin_code or ''
    }
    cart_items = Cart.objects.filter(user=request.user)
    
    # Calculate total price
    
    total = sum(item.product.price * item.quantity for item in cart_items )
    gst=total*0.18
    total_price = total + gst

    if request.method == 'POST':
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin_code = request.POST.get('pin_code')
        total_price = total_price  # Replace with actual price calculation

        order = Order.objects.create(
            user=request.user,
            full_name=profile.full_name,
            email=profile.email,
            phone=profile.phone,
            delivery_street=street,
            delivery_city=city,
            delivery_state=state,
            delivery_pin_code=pin_code,
            total_price=total_price
        )
        order.save()

        # PayPal Payment setup
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": request.build_absolute_uri('/payment-success/'),
                "cancel_url": request.build_absolute_uri('/payment-cancel/')
            },
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "Order Payment",
                        "sku": "001",
                        "price": str(total_price),
                        "currency": "USD",
                        "quantity": 1
                    }]
                },
                "amount": {
                    "total": str(total_price),
                    "currency": "USD"
                },
                "description": f"Payment for Order {order.id}"
            }]
        })

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    approval_url = str(link.href)
                    return redirect(approval_url)
        else:
            return render(request, 'payment_error.html')

    return render(request, 'checkout.html', {'profile': profile, 'delivery_address': delivery_address})

def clear_cart(user):
    Cart.objects.filter(user=user).delete()

def payment_success(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        # Mark the order as paid in your database
        clear_cart(request.user)
        messages.success(request, 'Order placed successfully! A confirmation email has been sent')
        return render(request, 'payment_success.html')
    else:
        return render(request, 'payment_error.html')






def payment_cancel(request):
    # Get the referer URL
    previous_url = request.META.get('HTTP_REFERER', '/')  # Fallback to home page if referer is not available
    
    # Optionally, you can add a message to notify the user
    messages.info(request, 'Payment has been cancelled.')
    
    return redirect(previous_url)


# def payment_cancel(request):
#     return render(request, 'payment_cancel.html')
