from . import views
from django.urls import path

app_name = 'book_app'

urlpatterns = [
    path('', views.BookListView.as_view(), name='index'),
    path('details/<pk>/', views.BookDetailView.as_view(), name='book_details'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('update/<pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('delete/<pk>/', views.BookDeleteView.as_view(), name='book_delete'),
    path('about/', views.AboutView.as_view(), name='about'),
]
