from rest_framework import serializers
from online_school.models import Course, Lesson
from users.models import Payments


class LessonSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор.'''
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(default=0)
    lesson = LessonSerializer(source='courses', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.courses.count()
