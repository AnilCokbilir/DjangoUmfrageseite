from unicodedata import name
from django.urls import path
from .views import index, results, umfrage_detail, vote

urlpatterns = [
path('', index, name='index'),
path('abstimmung/<str:slug>/', umfrage_detail, name='umfrage-detail'),
path('abstimmung/<str:slug>/vote/', vote, name="vote"),
path('abstimmung/<str:slug>/vote/results/', results, name="results")
]