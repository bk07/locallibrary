from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('authors/', views.AuthorListView.as_view(), name='All authors'),
    path('author/<int:pk>', views.AuthordetailsView.as_view(), name='author-detail'),


]


