from django.conf.urls import url
from .views import dogs

app_name = "dog"

urlpatterns = [
    url(r'^dogs/', dogs, name="dogs"),
]