from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index),
    path('login',views.index),
    path('info',views.index),
    path('login/info',views.index),
    path('register',views.patient_register),
    path('logout/',views.logout)
]

'''path('register/register',views.register),
    path('register/login/',views.login),
    path('register/login/login' , views.login),
    path('login/register',views.register),
    path('register/',views.register),
    path('register/verify/',views.verification),
    path('logout/',views.logout)'''