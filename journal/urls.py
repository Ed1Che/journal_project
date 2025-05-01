from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('new_entry/', views.create_entry, name='new_entry'),
    path('review_entries/', views.review_entries, name='review_entries'),
    path('edit_entry/<int:entry_id>/', views.edit_journal_entry, name='edit_entry'),
    path('delete_entry/<int:entry_id>/', views.delete_journal_entry, name='delete_entry'),
]