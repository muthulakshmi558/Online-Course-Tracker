from rest_framework import serializers
from .models import Course, Instructor

class CourseSerializer(serializers.ModelSerializer):
    total_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'total_lessons', 'instructor']

    # SerializerMethodField
    def get_total_lessons(self, obj):
        return obj.total_lessons

    # Validation: course title not empty
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Course title cannot be empty")
        return value


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'email']
