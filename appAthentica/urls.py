from django.urls import path
from .views import login_viw
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', login_viw, name="login"),
    path('logout', LogoutView.as_view(), name="logout")
]
