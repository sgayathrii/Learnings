from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView



# Create your views here.

class ListStudentAPIView(ListAPIView):
    """This endpoint list all of the available Student from the database"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CreateStudentAPIView(CreateAPIView):
    """This endpoint allows for creation of a Student record"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudentAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Student by passing in the id of the student to update"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DeleteStudentAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific student from the database"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
