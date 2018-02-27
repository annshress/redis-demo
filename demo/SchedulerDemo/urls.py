from django.urls import path

from .views import TasksHomeFormView, JobTemplateView

urlpatterns = [
    path('', TasksHomeFormView.as_view(), name='home'),
    # path('long/', LongTaskCreateView.as_view(), name='long_tasks'),
    path('job/<job>/', JobTemplateView.as_view(), name='view_job'),
]
