from django.urls import path
 from . import views

app_name = 'agency'

urlpatterns = [
    path('agency' , views.agency , name = 'agency'),
]