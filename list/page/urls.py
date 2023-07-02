from django.urls import path
from .views import index, SearchResultView


urlpatterns = [
    path('', index, name='index'),
    path('search/', SearchResultView.as_view(), name='search')
]