from django.contrib import admin
from django.utils.html import format_html
from solo.admin import SingletonModelAdmin

from settings.models import StartBalance


class SettingsAdmin(SingletonModelAdmin):

    readonly_fields = ('report_url',)

    def get_queryset(self, request):
        qs = super(SettingsAdmin, self).get_queryset(request)
        self.request = request
        return qs

    def report_url(self, obj):
        return format_html(f'<a class="btn button" style="margin-left:15px; color:white; background-color:green" target="_blank" href="{self.request.build_absolute_uri("/report")}">الذهاب للتقرير</a>')


admin.site.register(StartBalance, SettingsAdmin)
