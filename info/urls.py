
from django.urls import path
from info import  views
urlpatterns = [
    path('', views.home ),
   path('hire' , views.hire , name="hiree"),
    path('send' , views.sent ,name="sentt"),
]
