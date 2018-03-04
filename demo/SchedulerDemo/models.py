import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

GET = "get"
SAVE = "save"
COUPON_HASH_TYPES = (
    (GET, _("GET")),
    (SAVE, _("SAVE"))
)


class Coupon(models.Model):
    name = models.CharField(max_length=100, default="A coupon", blank = False)
    created_on = models.DateTimeField(_("Created On"),blank=False, default = datetime.datetime.now())
    type = models.CharField(_("Type"), max_length=5, choices=COUPON_HASH_TYPES)

class Task(models.Model):
    # A model to save information about an asynchronous task
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    job_id = models.CharField(max_length=128)
    result = models.CharField(max_length=128, blank=True, null=True)


class ScheduledTask(models.Model):
    # A model to save information about a scheduled task
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    # A scheduled task has a common job id for all its occurences
    job_id = models.CharField(max_length=128)


class ScheduledTaskInstance(models.Model):
    # A model to save information about instances of a scheduled task
    scheduled_task = models.ForeignKey('ScheduledTask', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=128, blank=True, null=True)