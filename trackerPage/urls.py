from django.urls import path, include 
from . import views


app_name = 'trackerPage'

urlpatterns = [
    path('', views.index, name='index'),
    path('maps/', views.maps, name='maps'),
    path('faqs/', views.faqs, name='faqs'),
    #path('trackerPage/', include('trackerPage.urls')),
]