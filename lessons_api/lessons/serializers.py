from lessons.models import Lessons, Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('short_name', 'name', 'position', 'imageUrl')

class LessonsSerializer(serializers.ModelSerializer):
    teacher_v2 = TeacherSerializer()
    class Meta:
        model = Lessons
        fields = ('name', 'description', 'place', 'teacher', 'startTime', 'endTime',
            'weekDay',
            'appointment_id',
            'service_id',
            'pay',
            'appointment',
            'teacher_v2',
            'color',
            'availability')
