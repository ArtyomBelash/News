from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsView.as_view(), name='index'),
    path('search', SearchView.as_view(), name='search_posts'),
]
