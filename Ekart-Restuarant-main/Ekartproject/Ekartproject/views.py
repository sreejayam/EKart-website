# from django.shortcuts import render, redirect
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from .forms import CreateUserForm
# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
#
# from Ekartapp.models import Category, Product
# from django.core.paginator import Paginator, EmptyPage, InvalidPage
#
#
# def registerPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = CreateUserForm()
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)
#
#                 return redirect('login')
#
#         context = {'form': form}
#         return render(request, 'register.html', context)
#
#
# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#
#             user = authenticate(request, username=username, password=password)
#
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.info(request, 'Username OR password is incorrect')
#
#         context = {}
#         return render(request, 'login.html', context)
#
#
# def logoutUser(request):
#     logout(request)
#     return redirect('login')
#
#
# # @login_required(login_url='login')
# def home(request, c_slug=None):
#     c_page = None
#     products_list = None
#     if c_slug != None:
#         c_page = get_object_or_404(Category, slug=c_slug)
#         products_list = Product.objects.all().filter(category=c_page, available=True)
#     else:
#         products_list = Product.objects.all().filter(available=True)
#     paginator = Paginator(products_list, 4)
#     try:
#         page = int(request.GET.get('page', '1'))
#     except:
#         page = 1
#     try:
#         products = paginator.page(page)
#     except(EmptyPage, InvalidPage):
#         products = paginator.page(paginator.num_pages)
#
#     return render(request, "category.html", {'category': c_page, 'products': products})
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.shortcuts import get_object_or_404
from Ekartapp.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests

CLIENT_ID = '449271567940-231ulmce7k5ergr43sksb5ljvtueer0p.apps.googleusercontent.com'
CLIENT_SECRET = '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'

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 4)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'products': products})

@csrf_exempt
def token_signin(request):
    if request.method == 'POST':
        token = request.POST.get('idtoken')
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            # ID token is valid. Get the user's Google Account ID from the decoded token.
            userid = idinfo['sub']
            email = idinfo['email']
            name = idinfo['name']

            # Here you can handle the user registration or login logic
            # For example, create or get the user and log them in
            # This is a placeholder implementation
            user = authenticate(request, username=email)
            if user is None:
                user = User.objects.create(username=email, email=email, first_name=name)
                user.set_unusable_password()
                user.save()

            login(request, user)

            return JsonResponse({'status': 'success', 'userid': userid, 'email': email})
        except ValueError:
            # Invalid token
            return JsonResponse({'status': 'error', 'message': 'Invalid token'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
