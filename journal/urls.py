from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('review_entries/', views.review_entries, name='review_entries'),
]