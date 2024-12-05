# from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from .forms import BookingForm
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedAndStaff
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    
    context = {'form': form}
    return render(request, 'book.html', context)

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('home')

def menu(request):
    if request.method == 'GET':
        menu_data = Menu.objects.all()
        main_data = {'menu': menu_data}
        return render(request, 'menu.html', main_data)
    else:
        return HttpResponse('Invalid request', status=403)

def display_menu_items(request, pk=None):
    if request.method == 'GET':
        if pk:
            menu_item = Menu.objects.filter(pk=pk).first()
        else:
            menu_item = None
        return render(request, 'menu_item.html', {'menu_item': menu_item})
    else:
        return HttpResponse('Invalid request', status=403)

class MenuItemAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedAndStaff]
    """Uncomment the line below after testing through API testing client."""
    """The session authentication interferes with the API testing client, \
    but allows for the use of the browsable API after login with credentials."""
    #authentication_classes = [SessionAuthentication, BasicAuthentication]    
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    search_fields = ['name', 'price']
    lookup_field = 'name'

    def get_queryset(self):
        try:
            if self.kwargs['name']:
                name = self.kwargs['name']
                return Menu.objects.filter(name=name)
        except KeyError: 
            return Menu.objects.all()

    
class BookingAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedAndStaff]
    """Uncomment the line below after testing"""
    """The session authentication interferes with the API testing client, \
    but allows for the use of the browsable API after login with credentials."""
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    search_fields = ['first_name', 'last_name']
    lookup_field = 'last_name'
    def get_queryset(self):
        try:
            if self.kwargs['last_name']:
                name = self.kwargs['last_name']
            return Booking.objects.filter(last_name=name)
        except KeyError: 
            return Booking.objects.all()
    
