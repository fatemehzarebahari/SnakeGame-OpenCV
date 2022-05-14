from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('',views.home, name='home'),
    path('sign_up/',views.sign_up, name='sign_up'),
    path('login/',views.login_page, name='login'),
    path('logout/',views.logout_user, name='logout'),
]
