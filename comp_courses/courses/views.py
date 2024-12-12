from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Student, Teacher
from .serializers import CourseSerializer, StudentSerializer, TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=False, methods=['get'])
    def report(self, request):
        report_data = {
            'total_courses': Course.objects.count(),
            'total_students': Student.objects.count(),
            'total_teachers': Teacher.objects.count(),
        }
        return Response(report_data)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
