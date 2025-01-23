from django.contrib import admin
from app1.models import works,contact_form_info,projects

# Register your models here.
@admin.register(works)
class works(admin.ModelAdmin):
    list_display=[
        'work_name'
    ]
@admin.register(contact_form_info)
class contact_forms(admin.ModelAdmin):
    list_display=[
        'name'
    ]
@admin.register(projects)
class project(admin.ModelAdmin):
    list_display=[
        'id'
    ]