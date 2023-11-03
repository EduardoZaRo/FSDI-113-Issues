from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
);
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.core.exceptions import PermissionDenied

from .models import Issue, Status
from accounts.models import Team
class IssueListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Issue
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archived_status = Team.objects.get(name=self.request.user.team)
        context["issue_list"] = Issue.objects.filter(
            reporter__team=archived_status
        ).order_by("created_on").reverse()
        return context

class IssueCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["summary", "description", "reporter","assignee",  "status"]
    def test_func(self):
        return str(self.request.user.role) == "product owner"
    
class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["summary", "description", "reporter","assignee",  "status"]
    def test_func(self):
        return str(self.request.user.role) == "product owner"

class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("list")
    def test_func(self):
        return str(self.request.user.role) == "scrum master"
    
class IssueAssignView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/assign.html"
    model = Issue
    fields = ["assignee"]
    def test_func(self):
        return str(self.request.user.role) == "scrum master"

class IssueUpdateStatusView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/assign.html"
    model = Issue
    fields = ["status"]
    def test_func(self):
        return str(self.request.user.role) == "developer"
    
    