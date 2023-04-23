from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User

@api_view(['POST'])
def auth(request):
    # Your authentication code here
    return Response('Authenticated')

@api_view(['POST'])
def add_user(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    user = User(name=name, email=email, password=password)
    user.save()
    return Response('User added successfully')

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    data = [{'name': user.name, 'email': user.email} for user in users]
    return Response(data)

@api_view(['PUT'])
def edit_user(request, id):
    user = User.objects.get(id=id)
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    user.name = name
    user.email = email
    user.password = password
    user.save()
    return Response('User updated successfully')