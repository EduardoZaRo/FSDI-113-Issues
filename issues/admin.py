from django.contrib import admin

# Register your models here.
from .models import Issue 

class PostAdmin(admin.ModelAdmin):
    list_display = ["summary","description","reporter","assignee","created_on","status"]
    

admin.site.register(Issue, PostAdmin)