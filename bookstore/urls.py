from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('' , views.bookstore, name='bookstore'),
    path('logout', views.logout_view , name='logout'),
]