from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Project, Risk

admin.site.register(Project)
admin.site.register(Risk, SimpleHistoryAdmin)
