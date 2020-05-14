from django.urls import path
from lessons.views import ListLessonsView

urlpatterns = [
    path('lessons/', ListLessonsView.as_view(), name="lessons-all")
]
