from django.contrib import admin
from main.models import ApplicationCategory, Application, ApplicationStatus

# Register your models here.

admin.site.register(ApplicationCategory)
admin.site.register(ApplicationStatus)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'imageofapp', 'description', 'category', 'status', 'created_timestamp', 'author')
    readonly_fields = ('created_timestamp',)
    ordering = ('created_timestamp',)
    search_fields = ('name',)

