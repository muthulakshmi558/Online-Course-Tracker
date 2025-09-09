from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Instructor
from .serializers import CourseSerializer, InstructorSerializer
from django.shortcuts import render
from .models import Course, Instructor

# Courses (CBV)
class CourseListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        instructor_id = self.request.query_params.get('instructor_id')
        if instructor_id:
            queryset = queryset.filter(instructor_id=instructor_id)
        return queryset


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

def course_home(request):
    courses = Course.objects.all()
    instructors = Instructor.objects.all()
    return render(request, "courses/course_list.html", {
        "courses": courses,
        "instructors": instructors
    })
# Instructors (FBV)
@api_view(['GET', 'POST'])
def instructor_list_create(request):
    if request.method == 'GET':
        instructors = Instructor.objects.all()
        serializer = InstructorSerializer(instructors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
