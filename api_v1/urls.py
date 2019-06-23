from django.urls import path

from api_v1.views import Login

urlpatterns = [
    path('login/', Login.as_view())
]

