from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    # path('books/', book_list, name='book_list'),
    # path('books/<int:book_id>/', book_detail, name='book_detail'),
    path('books/', BookListView.as_view(), name = 'book_list'),
    path('books/<int:pk>/', BookDetails.as_view(), name = 'book_detail'),
    path('books/<int:pk>/edit', BookUpdate.as_view(), name = 'book_edit'),
    path('books/add', BookCreate.as_view(), name = 'book_add'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
