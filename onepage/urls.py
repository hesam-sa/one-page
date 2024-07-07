from django.contrib import admin
from django.urls import path,include
from onepage.views import index_view

urlpatterns = [
    
    # path('onepage',include('onepage.urls'))
    path('',index_view)
]