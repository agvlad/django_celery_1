from django.urls import path
from .views import GetTaskView, CreateTaskView

urlpatterns = [
    path('task/', CreateTaskView.as_view()),
    path('task/<task_id>', GetTaskView.as_view()),
]


def Test():
    pass
