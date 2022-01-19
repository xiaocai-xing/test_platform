from django.contrib import admin
from user_app.models import Project,Module

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','describe','status','creat_time','id']

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'creat_time', 'project','id']

# Register your models here.
# Django自带的admin的后台
admin.register(Project,site=Project)
admin.register(Module,site=Module)

