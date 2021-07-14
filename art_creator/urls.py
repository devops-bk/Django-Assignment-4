from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artBlog.urls')),
    path('users/', include('users.urls')),
    path('user/', include('django.contrib.auth.urls')),
]
