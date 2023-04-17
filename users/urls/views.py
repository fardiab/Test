from django.urls import path, include
from users.views import *

from core.views import *

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login, name="login"),
    path("add_instagram/", get_instagram, name="add_instagram"),
]
