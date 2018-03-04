import datetime

from django.apps import AppConfig


class SchedulerdemoConfig(AppConfig):
    name = 'SchedulerDemo'

    def ready(self):
        import django_rq
        from SchedulerDemo.tasks import change_coupon_type
        timenow = datetime.datetime.now()
        scheduler = django_rq.get_scheduler('default')
        job = scheduler.schedule(
            scheduled_time=timenow,
            func=change_coupon_type,
            interval=5,
        )
