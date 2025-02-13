from django.urls import path
from .views import IssueCrudView
issue_crud = IssueCrudView()

urlpatterns = [
    path('', issue_crud.list, name='issue-list'),
    path('create/', issue_crud.create, name='issue-create'),
    path('<int:pk>/', issue_crud.detail, name='issue-detail'),
    path('<int:pk>/update/', issue_crud.update, name='issue-update'),
    path('<int:pk>/delete/', issue_crud.delete, name='issue-delete'),
    path('<int:pk>/status/', issue_crud.update_status, name='issue-update-status'),
]