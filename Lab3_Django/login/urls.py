from django.urls import path

import login.views
from login import views

urlpatterns = [
    path('', views.Login.as_view(), name="login"),
    path('logout', login.views.logout_view, name="logout")
]
