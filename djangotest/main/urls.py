from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index),
    path('accounts/', include('django.contrib.auth.urls'))
]
