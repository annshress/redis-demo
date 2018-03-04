from django.urls import path

from SchedulerDemo.views import CouponView, CouponDetailView
from .views import TasksHomeFormView, JobTemplateView

urlpatterns = [
    path('', TasksHomeFormView.as_view(), name='home'),
    # path('long/', LongTaskCreateView.as_view(), name='long_tasks'),
    path('job/<job>/', JobTemplateView.as_view(), name='view_job'),
    path('coupon/', CouponView.as_view(), name='coupon_detail'),
    path('coupon/<coupon_id>/', CouponDetailView.as_view(), name='a_coupon_detail')

]
