from django.contrib import admin
from Projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    popuprepopulated_fields = {"slug": ("name", )}


admin.site.register(Project, ProjectAdmin)
