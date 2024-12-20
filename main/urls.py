from django.urls import path # step 12  
from main.views import main

urlpatterns = [
    path('main/', main, name='main')
]
