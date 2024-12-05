from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('menu/', views.menu, name="menu"),
    path('menu/<int:pk>/', views.display_menu_items, name="menu_item"),
    path('apis/menu-items-api/<str:name>', views.MenuItemAPI.as_view({'post':'create',\
    'get':'list', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})\
    , name='menu-items-api'),
    path('apis/booking-api/<str:last_name>', views.BookingAPI.as_view({'post':'create','get':'list'\
    , 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})\
    , name='booking-api'),

]