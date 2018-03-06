import datetime

from django.apps import AppConfig


class SchedulerdemoConfig(AppConfig):
    name = 'SchedulerDemo'

    def ready(self):
        import django_rq
        from SchedulerDemo.tasks import change_coupon_type

        scheduler = django_rq.get_scheduler('default')
        print(scheduler.get_jobs())
        if bool(scheduler.get_jobs()):
            pass
        else:
            job = scheduler.schedule(
                scheduled_time=datetime.datetime.now(),
                func=change_coupon_type,
                interval=70,
                )
        print (scheduler.get_jobs())

