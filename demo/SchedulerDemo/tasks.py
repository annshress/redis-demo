import datetime
import requests
from django.utils import timezone

from SchedulerDemo.models import Coupon
from .models import Task, ScheduledTask, ScheduledTaskInstance, GET, SAVE
from rq import get_current_job
from django_rq import job
import time

@job
def get_url_words(url):
    # This creates a Task instance to save the job instance and job result
    job = get_current_job()

    task = Task.objects.create(
        job_id=job.get_id(),
        name=url
    )
    response = requests.get(url)
    task.result = len(response.text)
    task.save()
    return task.result


@job
def scheduled_get_url_words(url):
    """
    This creates a ScheduledTask instance for each group of
    scheduled task - each time this scheduled task is run
    a new instance of ScheduledTaskInstance will be created
    """
    job = get_current_job()

    task, created = ScheduledTask.objects.get_or_create(
        job_id=job.get_id(),
        name=url
    )
    response = requests.get(url)
    response_len = len(response.text)
    ScheduledTaskInstance.objects.create(
        scheduled_task=task,
        result = response_len,
    )
    return response_len


@job
def get_title_change(url):

    # job = get_current_job()
    #
    # task = Task.objects.get(
    #     job_id=job.get_id(),
    #     name=url
    # )
    # task.name = "this task is scheduled"
    # task.save()
    # return task.result
    # This creates a Task instance to save the job instance and job result
    job = get_current_job()
    time.sleep(4)
    task = Task.objects.order_by('-id').last()
    task.result = task.name
    Task.objects.create(
        job_id=job.get_id(),
        name=task.name + "s"
    )

    return task.result

@job
def change_coupon_type():
    timenow = timezone.now()
    count=0
    for coupon in Coupon.objects.filter(type=SAVE):
        if timenow - coupon.created_on >= datetime.timedelta(minutes=2):
            coupon.type = GET
            count +=1
            coupon.save()
    return count

