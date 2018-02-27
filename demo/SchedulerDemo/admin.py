from django.contrib import admin

# Register your models here.
from SchedulerDemo.models import Task, ScheduledTask, ScheduledTaskInstance


class TaskAdmin(admin.ModelAdmin):
    list_display = ['created_on', 'job_id', 'result', 'name']


class ScheduledTaskAdmin(admin.ModelAdmin):
    list_display = ['created_on', 'job_id', 'name']


class ScheduledTaskInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)
admin.site.register(ScheduledTask, ScheduledTaskAdmin)
admin.site.register(ScheduledTaskInstance, ScheduledTaskInstanceAdmin)
