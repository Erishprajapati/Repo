from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job, Company, Application
from .serializers import JobSerializer, CompanySerializer, ApplicationSerializer
import json
from .permissions import *

class JobView(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk = None):
        if pk:
            job = Job.objects.get(pk = pk)
            serializer = JobSerializer(job)
            return Response(serializer.data)
        else:
            jobs = Job.objects.all()
            serializer = JobSerializer(jobs, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        # Log the incoming request data (for debugging purposes)
        print("Received JSON Data:", request.data)
        
        # Create the serializer instance with the received data
        serializer = JobSerializer(data=request.data)
        
        # Check if the data is valid and save if true
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            # Return error if the data is not valid
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        job = Job.objects.get(pk = pk)
        serializer = JobSerializer(job, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.error, status = status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, pk):
        try:
            job = Job.objects.get(pk = pk)
            job.delete()
            return Response({"detail": "job deleted successfully"}, status = status.HTTP_204_NO_CONTENT)
        except Job.DoesNotExist:
            return Response({"detail": "job doesnt exist"}, status = status.HTTP_400_BAD_REQUEST)
        
class CompanyView(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk = None):

        if pk:
            company = Company.objects.get(pk = pk)
            serializer = CompanySerializer(company)
            return Response(serializer.data)
        else:
            company = Company.objects.all()
            serializer = CompanySerializer(company, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,{"Details": "Company has been registered."})
        return Response(serializer.errors, {"Details" : "Failed to register.."})

class ApplicationView(APIView):
    # permission_classes = [IsAdminOrReadOnly]
    def get(self, request):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)  # Fixed serializer mistake
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Fixed `serializer.error`
