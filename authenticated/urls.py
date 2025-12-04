from . import views
from django.urls import path

urlpatterns = [
    path('login_page', views.login_page, name='login_page'),
    path('logout_page', views.logout_page, name='logout_page'),
]