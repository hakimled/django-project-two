from django.urls import path
from . import views
app_name = 'news'
urlpatterns = [
    path('', views.news , name='news'),
    path('create/' , views.add_member  , name='greet'),
]