from django.contrib import admin
from .models import Project
from .models import info

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated', 'id')
class InfoAdmin(admin.ModelAdmin):
    readonly_fields =('name', )

admin.site.register(Project, ProjectAdmin)
admin.site.register(info)