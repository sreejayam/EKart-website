# # from django.shortcuts import render
# # from django.http import HttpResponse
# #
# # import razorpay
# # from django.shortcuts import render, redirect, get_object_or_404
# # from Ekartapp.models import Product
# # from cart.models import *
# # from django.core.exceptions import ObjectDoesNotExist
# #
# #
# # client = razorpay.Client(auth=("rzp_test_dD3s7LqfVjjw7f", "j9yVuy7FQKOdoZit1N4jZimq"))
# #
# #
# # def testing(request):
# #
# #     return render(request, 'order.html', {})
# # def _cart_id(request):
# #     cart = request.session.session_key
# #     if not cart:
# #         cart = request.session.create()
# #     return cart
# # def cart_detail(request, total=0, counter=0, cart_items=None):
# #     try:
# #         cart = Cart.objects.get(cart_id=_cart_id(request))
# #         cart_items = CartItem.objects.filter(cart=cart, active=True)
# #         for cart_item in cart_items:
# #             total += (cart_item.product.price * cart_item.quantity)
# #             counter += cart_item.quantity
# #
# #     except ObjectDoesNotExist:
# #         pass
# #     return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))
# #
# #
# #
# #
# # def create_order(request):
# #     if request.method == 'POST':
# #         name = request.POST.get('name')
# #         phone = request.POST.get('phone')
# #         email = request.POST.get('email')
# #         address1 = request.POST.get('address1')
# #         address2 = request.POST.get('address2')
# #         city = request.POST.get('city')
# #         state = request.POST.get('state')
# #         pincode = request.POST.get('pincode')
# #
# #         cart = Cart.objects.get(cart_id=_cart_id(request))
# #         cart_items = CartItem.objects.filter(cart=cart, active=True)
# #
# #         total_amount = 0
# #         for cart_item in cart_items:
# #             total_amount += (cart_item.product.price * cart_item.quantity)
# #
# #         # Adding shipping charge if total is less than 500
# #         if total_amount < 500:
# #             total_amount += 50  # Adding shipping charge of Rs. 50
# #
# #         total_amount_in_paisa = int(total_amount * 100)  # Convert to smallest currency unit
# #
# #         order_currency = 'INR'
# #         order_receipt = 'order_rcptid_11'
# #         notes = {
# #             'Shipping address': f"{address1}, {address2}, {city}, {state}, {pincode}"
# #         }
# #
# #         # CREATING ORDER
# #         response = client.order.create(
# #             dict(amount=total_amount_in_paisa, currency=order_currency, receipt=order_receipt, notes=notes,
# #                  payment_capture='0'))
# #         order_id = response['id']
# #         order_status = response['status']
# #
# #         if order_status == 'created':
# #             context = {
# #                 'product_id': cart_items[0].product.id if cart_items else None,
# #                 'price': total_amount,
# #                 'name': name,
# #                 'phone': phone,
# #                 'address1': address1,
# #                 'address2': address2,
# #                 'city': city,
# #                 'state': state,
# #                 'pincode': pincode,
# #                 'email': email,
# #                 'order_id': order_id
# #             }
# #             return render(request, 'confirm_order.html', context)
# #         else:
# #             return HttpResponse('<h1>Error in create order function</h1>')
# #
# #     else:
# #         return HttpResponse('<h1>Invalid request method</h1>')
# #
# # def payment_status(request):
# #
# #     response = request.POST
# #
# #     params_dict = {
# #         'razorpay_payment_id' : response['razorpay_payment_id'],
# #         'razorpay_order_id' : response['razorpay_order_id'],
# #         'razorpay_signature' : response['razorpay_signature']
# #     }
# #
# #
# #     # VERIFYING SIGNATURE
# #     try:
# #         status = client.utility.verify_payment_signature(params_dict)
# #         return render(request, 'order_summary.html', {'status': 'Payment Successful'})
# #     except:
# #         return render(request, 'order_summary.html', {'status': 'Payment Faliure!!!'})
# #
#
#
# from django.http import HttpResponse
# from django.shortcuts import render, redirect, get_object_or_404
# from Ekartapp.models import Product
# from payments.models import Order,OrderItem
# from cart.models import Cart, CartItem
# from django.core.exceptions import ObjectDoesNotExist
# import razorpay
#
# client = razorpay.Client(auth=("rzp_test_dD3s7LqfVjjw7f", "j9yVuy7FQKOdoZit1N4jZimq"))
#
# def testing(request):
#     return render(request, 'order.html', {})
#
# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart
#
# def cart_detail(request, total=0, counter=0, cart_items=None):
#     try:
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_items = CartItem.objects.filter(cart=cart, active=True)
#         for cart_item in cart_items:
#             total += (cart_item.product.price * cart_item.quantity)
#             counter += cart_item.quantity
#
#     except ObjectDoesNotExist:
#         pass
#     return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))
#
# def create_order(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         address1 = request.POST.get('address1')
#         address2 = request.POST.get('address2')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         pincode = request.POST.get('pincode')
#
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_items = CartItem.objects.filter(cart=cart, active=True)
#
#         total_amount = 0
#         for cart_item in cart_items:
#             total_amount += (cart_item.product.price * cart_item.quantity)
#
#         # Adding shipping charge if total is less than 500
#         if total_amount < 500:
#             total_amount += 50  # Adding shipping charge of Rs. 50
#
#         total_amount_in_paisa = int(total_amount * 100)  # Convert to smallest currency unit
#
#         order_currency = 'INR'
#         order_receipt = 'order_rcptid_11'
#         notes = {
#             'Shipping address': f"{address1}, {address2}, {city}, {state}, {pincode}"
#         }
#
#         # CREATING ORDER
#         response = client.order.create(
#             dict(amount=total_amount_in_paisa, currency=order_currency, receipt=order_receipt, notes=notes,
#                  payment_capture='0'))
#         order_id = response['id']
#         order_status = response['status']
#
#         if order_status == 'created':
#             # Payment successful, create order instance
#             order = Order.objects.create(
#                 order_id=order_id if cart_items else None,
#                 name=name,
#                 phone=phone,
#                 email=email,
#                 address1=address1,
#                 address2=address2,
#                 city=city,
#                 state=state,
#                 pincode=pincode,
#                 total_amount=total_amount
#             )
#
#             # Add order items
#             for cart_item in cart_items:
#                 OrderItem.objects.create(
#                     order=order,
#                     product=cart_item.product,
#                     quantity=cart_item.quantity,
#                     price=cart_item.product.price
#                 )
#
#             # Redirect to order confirmation page or do whatever you need to do next
#             context = {
#                 'product_id': cart_items[0].product.id if cart_items else None,
#                 'price': total_amount,
#                 'name': name,
#                 'phone': phone,
#                 'address1': address1,
#                 'address2': address2,
#                 'city': city,
#                 'state': state,
#                 'pincode': pincode,
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
# def payment_status(request):
#     response = request.POST
#     params_dict = {
#         'razorpay_payment_id': response['razorpay_payment_id'],
#         'razorpay_order_id': response['razorpay_order_id'],
#         'razorpay_signature': response['razorpay_signature']
#     }
#
#     # VERIFYING SIGNATURE
#     try:
#         status = client.utility.verify_payment_signature(params_dict)
#         return render(request, 'order_summary.html', {'status': 'Payment Successful'})
#     except:
#         return render(request, 'order_summary.html', {'status': 'Payment Failure!!!'})
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Ekartapp.models import Product
from payments.models import Order, OrderItem
from cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
import razorpay
from django.core.mail import send_mail
import logging

# Set up logging
logger = logging.getLogger(__name__)
client = razorpay.Client(auth=("rzp_test_dD3s7LqfVjjw7f", "j9yVuy7FQKOdoZit1N4jZimq"))
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
def confirm_cash_on_delivery(request):
    return render(request, 'confirm_cash_on_delivery.html')
@csrf_exempt
def confirm_online_payment(request):
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

        # Adding shipping charge if total is less than 500
        if total_amount < 500:
            total_amount += 50  # Adding shipping charge of Rs. 50

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
                'address1': address1,
                'address2': address2,
                'city': city,
                'state': state,
                'pincode': pincode,
                'email': email,
                'order_id': order_id
            }
            return render(request, 'confirm_order.html', context)
        else:
            return HttpResponse('<h1>Error in create order function</h1>')

    else:
        return HttpResponse('<h1>Invalid request method</h1>')

def handle_confirm_order(request):
    # Your existing logic goes here

    # Assuming you have confirmed the order and want to send an email
    send_mail(
        'SavaariFoods: Order Confirmation',
        'Your order has been placed successfully',
        settings.EMAIL_HOST_USER,  # From email address
        [request.user.email],      # To email address, assuming request.user.email exists
        fail_silently=False,       # Set to True to suppress errors if email fails
    )

    return render(request, 'thanks.html', {'status': 'Order Confirmed'})
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

        # Adding shipping charge if total is less than 500
        if total_amount < 500:
            total_amount += 50  # Adding shipping charge of Rs. 50

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
                'address1': address1,
                'address2': address2,
                'city': city,
                'state': state,
                'pincode': pincode,
                'email': email,
                'order_id': order_id
            }
            return render(request, 'payment_method.html', context)
        else:
            return HttpResponse('<h1>Error in create order function</h1>')

    else:
        return HttpResponse('<h1>Invalid request method</h1>')

# def payment_status(request):
#     response = request.POST
#     params_dict = {
#         'razorpay_payment_id': response['razorpay_payment_id'],
#         'razorpay_order_id': response['razorpay_order_id'],
#         'razorpay_signature': response['razorpay_signature']
#     }
#
#     # VERIFYING SIGNATURE
#     try:
#         status = client.utility.verify_payment_signature(params_dict)
#
#         # Fetch the order details from the session or a hidden form field
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         address1 = request.POST.get('address1')
#         address2 = request.POST.get('address2')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         pincode = request.POST.get('pincode')
#         total_amount = request.POST.get('total_amount')
#
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_items = CartItem.objects.filter(cart=cart, active=True)
#
#         # Payment successful, create order instance
#         order = Order.objects.create(
#             order_id=params_dict['razorpay_order_id'],
#             name=name,
#             phone=phone,
#             email=email,
#             address1=address1,
#             address2=address2,
#             city=city,
#             state=state,
#             pincode=pincode,
#             total_amount=total_amount
#         )
#
#         # Add order items
#         for cart_item in cart_items:
#             OrderItem.objects.create(
#                 order=order,
#                 product=cart_item.product,
#                 quantity=cart_item.quantity,
#                 price=cart_item.product.price
#             )
#
#         # Clear cart items after order is created
#         cart_items.update(active=False)
#         # Sending order confirmation email
#         subject = 'Order Confirmation-Savaari'
#         message = f'Thank you for your order, {name}!\n\nYour order has been placed successfully.\nOrder ID: {order.order_id}\nTotal Amount: {total_amount}\n\nShipping Address:\n{address1}, {address2}, {city}, {state}, {pincode}'
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email]
#         send_mail(subject, message, email_from, recipient_list)
#         return render(request, 'order_summary.html', {'status': 'Payment Successful', 'order': order})
#     except:
#         return render(request, 'order_summary.html', {'status': 'Payment Failure!!!'})

def payment_status(request):
    response = request.POST

    params_dict = {
        'razorpay_payment_id': response.get('razorpay_payment_id'),
        'razorpay_order_id': response.get('razorpay_order_id'),
        'razorpay_signature': response.get('razorpay_signature')
    }

    try:
        status = client.utility.verify_payment_signature(params_dict)
        # If payment is successful, send an email to the receiver
        send_mail(
            'Payment Successful: Savaari',
            'Your payment has been successfully processed. Thank you for your purchase!',
            settings.EMAIL_HOST_USER,
            ['sreejayam16@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'order_summary.html', {'status': 'Payment Successful'})
    except Exception as e:
        logger.error(f"Payment verification failed: {e}")
        # If payment verification fails, send an email to the receiver
        send_mail(
            'Payment Failed: Savaari',
            'Your payment has failed. Please try again or contact support if you have any questions.',
            settings.EMAIL_HOST_USER,
            ['sreejayam16@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'order_summary.html', {'status': 'Payment Failure!!!'})