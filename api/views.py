from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Person, Student
from .serializers import PersonSerializer, StudentSerializer


@api_view(["GET"])
def getdata(request):
    persons = Person.objects.all()
    seralizer = PersonSerializer(persons, many=True)
    return Response(seralizer.data)


@api_view(["POST"])
def addPerson(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def getstudentdata(request):
    student = Student.objects.all()
    seralizer = StudentSerializer(student, many=True)
    return Response(seralizer.data)


@api_view(["POST"])
def addStudent(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
def updateStudent(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=404)

    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
