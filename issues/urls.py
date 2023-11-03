from django.urls import path
from issues import views

urlpatterns = [
    path("", views.IssueListView.as_view(), name="list"),
    path("new/", views.IssueCreateView.as_view(), name="new"),
    path("<int:pk>/edit/", views.IssueUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/",views.IssueDeleteView.as_view(),name="delete"),
    path("<int:pk>/assign/",views.IssueAssignView.as_view(),name="assign"),
    path("<int:pk>/update-status/",views.IssueUpdateStatusView.as_view(),name="update-status"),
]