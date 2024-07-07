from django.contrib import admin
from django.urls import path,include
from onepage.views import http_test,json_test

urlpatterns = [
    
    # path('onepage',include('onepage.urls'))
    path('http_test/', http_test),
    path('json_test/', json_test)  # this route will return a JSON response with the key 'name' and the value 'ali'
]