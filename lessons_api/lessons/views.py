from django.shortcuts import render
from rest_framework import generics
from lessons.models import Lessons
from lessons.serializers import LessonsSerializer

class ListLessonsView(generics.ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
