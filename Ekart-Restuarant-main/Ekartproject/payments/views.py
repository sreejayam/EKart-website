from django.shortcuts import render
from django.http import HttpResponse

import razorpay
from django.shortcuts import render, redirect, get_object_or_404
from Ekartapp.models import Product
from cart.models import *
from django.core.exceptions import ObjectDoesNotExist


client = razorpay.Client(auth=("rzp_test_dD3s7LqfVjjw7f", "j9yVuy7FQKOdoZit1N4jZimq"))


def testing(request):

    return render(request, 'order.html', {})
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))


# def create_order(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_items = CartItem.objects.filter(cart=cart, active=True)
#
#         total_amount = 0
#         for cart_item in cart_items:
#             total_amount += (cart_item.product.price * cart_item.quantity)
#
#         total_amount_in_paisa = int(total_amount * 100)  # Convert to smallest currency unit
#
#         order_currency = 'INR'
#         order_receipt = 'order_rcptid_11'
#         notes = {'Shipping address': 'Bommanahalli, Bangalore'}
#
#         # CREATING ORDER
#         response = client.order.create(
#             dict(amount=total_amount_in_paisa, currency=order_currency, receipt=order_receipt, notes=notes,
#                  payment_capture='0'))
#         order_id = response['id']
#         order_status = response['status']
#
#         if order_status == 'created':
#             context = {
#                 'product_id': cart_items[0].product.id if cart_items else None,
#                 'price': total_amount,
#                 'name': name,
#                 'phone': phone,
#                 'email': email,
#                 'order_id': order_id
#             }
#             return render(request, 'confirm_order.html', context)
#         else:
#             return HttpResponse('<h1>Error in create order function</h1>')
#
#     else:
#         return HttpResponse('<h1>Invalid request method</h1>')
#
def create_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')

        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        total_amount = 0
        for cart_item in cart_items:
            total_amount += (cart_item.product.price * cart_item.quantity)

        total_amount_in_paisa = int(total_amount * 100)  # Convert to smallest currency unit

        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {
            'Shipping address': f"{address1}, {address2}, {city}, {state}, {pincode}"
        }

        # CREATING ORDER
        response = client.order.create(
            dict(amount=total_amount_in_paisa, currency=order_currency, receipt=order_receipt, notes=notes,
                 payment_capture='0'))
        order_id = response['id']
        order_status = response['status']

        if order_status == 'created':
            context = {
                'product_id': cart_items[0].product.id if cart_items else None,
                'price': total_amount,
                'name': name,
                'phone': phone,
                'address1':address1,
                'address2':address2,
                'city':city,
                'state':state,
                'pincode':pincode,
                'email': email,
                'order_id': order_id
            }
            return render(request, 'confirm_order.html', context)
        else:
            return HttpResponse('<h1>Error in create order function</h1>')

    else:
        return HttpResponse('<h1>Invalid request method</h1>')
def payment_status(request):

    response = request.POST

    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }


    # VERIFYING SIGNATURE
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'order_summary.html', {'status': 'Payment Successful'})
    except:
        return render(request, 'order_summary.html', {'status': 'Payment Faliure!!!'})