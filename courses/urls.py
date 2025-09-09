from django.urls import path
from .views import (
    CourseListCreateAPIView,
    CourseDetailAPIView,
    instructor_list_create,
    course_home
)


urlpatterns = [
    # HTML page
    path('', course_home, name='course-home'),

    # Courses API (CBV)
    path('api/courses/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('api/courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),

    # Instructors API (FBV)
    path('api/instructors/', instructor_list_create, name='instructor-list-create'),
]