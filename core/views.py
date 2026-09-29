from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import JobSerializer


def home(request):
    return HttpResponse("Hello zecpath backend")


jobs = [
    {
        "title": "Python Developer",
        "company": "ABC Technologies",
        "location": "Chennai"
    }
]


@api_view(['GET'])
def job_list(request):
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_test(request):
    return Response({
        "message": "User API working",
        "user": "Abhishek"
    })    

@api_view(['POST'])
def job_create(request):
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        return Response(serializer.validated_data)

    return Response(serializer.errors)    