from django.urls import path,include
from .views import BookDetailsView, BookListView
urlpatterns = [
    path('', BookListView.as_view(), name = 'books'),
    path('<int:pk>', BookDetailsView.as_view(), name = 'details'),
]
