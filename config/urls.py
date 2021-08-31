
from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "First project"
admin.site.site_title = "First project"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("dog.urls"))
]

#
