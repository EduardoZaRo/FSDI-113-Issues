from django import forms

from accounts.models import CustomUser, Role
from .models import Issue
from django.contrib.auth import get_user_model

class FormAssignDeveloper(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'assignee',       
        ]        
    
    def __init__(self, *args, **kwargs):
        role = Role.objects.get(name="developer")
        super(FormAssignDeveloper, self).__init__(*args, **kwargs)        
        self.fields['assignee'].queryset = CustomUser.objects.filter(role=role)