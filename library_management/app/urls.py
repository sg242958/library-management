from django.urls import path
from .views import (
    BookCreateView, BookListView, 
    MemberCreateView, MemberListView, 
    BorrowBookView, ReturnBookView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='list-books'),
    path('books/add/', BookCreateView.as_view(), name='add-book'),
    path('members/', MemberListView.as_view(), name='list-members'),
    path('members/add/', MemberCreateView.as_view(), name='add-member'),
    path('borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
]