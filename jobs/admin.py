from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'status', 'user', 'date_applied')
    list_filter = ('status',)
    search_fields = ('company', 'role')

    # Make all fields read-only
    readonly_fields = ('user', 'company', 'role', 'status', 'date_applied', 'notes')

    # Disable add permission
    def has_add_permission(self, request):
        return False

    # Disable delete permission
    def has_delete_permission(self, request, obj=None):
        return False

    # Disable edit permission
    def has_change_permission(self, request, obj=None):
        return False
