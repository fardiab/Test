from django.urls import path, include
from users.apis import *


urlpatterns = [
    path('register-api/', RegisterView.as_view(), name='register-api'),
]