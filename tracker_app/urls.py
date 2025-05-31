from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-transaction/', views.add_transaction, name='add_transaction'),
    path('edit-transaction/<int:transaction_id>/', views.edit_transaction, name='edit_transaction'),
    path('delete-transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),

    path('add-goal/', views.add_goal, name='add_goal'),
    path('edit-goal/<int:goal_id>/', views.edit_goal, name='edit_goal'),
    path('delete-goal/<int:goal_id>/', views.delete_goal, name='delete_goal'),

    path('logout/', views.logout_view, name='logout'),
]
