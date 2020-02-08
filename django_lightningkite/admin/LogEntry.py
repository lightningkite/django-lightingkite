from django.contrib import admin
from django.contrib.admin.models import LogEntry

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'content_type', 'user',
                    'user_email', 'action_time',)
    list_filter = (
        (
            'user',
            admin.RelatedOnlyFieldListFilter
        ),
        'content_type',
    )
    search_fields = ['user__email', 'change_message',
                     'content_type__model', 'content_type__app_label']
    list_select_related = ('user',)
    readonly_fields = ('content_type',
                       'user',
                       'user_id',
                       'user_email',
                       'action_time',
                       'object_id',
                       'object_repr',
                       'action_flag',
                       'change_message')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return request.method == 'GET'

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass

    def get_actions(self, request):
        actions = super(LogEntryAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def user_id(self, obj):
        return obj.user.pk

    def user_email(self, obj):
        return obj.user.email
