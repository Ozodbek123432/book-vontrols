from django.contrib import admin
from django.urls import path, include
from book_contoler.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', BookCrud.as_view({'get': 'list'})),
    path('create/', BookCrud.as_view({'post':'create'}),name='creat'),
    path('update/<int:pk>/', BookCrud.as_view({'put':'update'}),name='update'),
    path('delete/<int:pk>/', BookCrud.as_view({'delete':'destroy'}),name='delete'),
]