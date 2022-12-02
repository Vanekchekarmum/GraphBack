from django.urls import path, include
from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('graph', TodoListApiView.as_view()),
]