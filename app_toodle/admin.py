from django.contrib import admin
from .models import UserProfile, Task


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'user__email', 'phone')
    list_filter = ('user__is_active',)
    readonly_fields = ('user',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'get_status_display')
    list_filter = ('status', 'user')
    search_fields = ('title', 'user__username')
    list_editable = ('status',)
    list_per_page = 20
    ordering = ('-id',)
    
    def get_status_display(self, obj):
        return '✓ Completed' if obj.status else '○ Pending'
    get_status_display.short_description = 'Status Display'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user')
    
    # Allow filtering tasks by current user if not superuser
    def get_list_filter(self, request):
        if request.user.is_superuser:
            return self.list_filter
        return ('status',)
    
    # Limit queryset to user's own tasks if not superuser
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.select_related('user')
        return qs.filter(user=request.user).select_related('user')
