
from django.contrib import admin
from django.urls import path, include
from library.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('library.urls')),
    path('', home, name='home'),
    path('books/', include('library.urls')),
]
