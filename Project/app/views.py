from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

@api_view(['POST'])
def auth(request):
    if request.method == 'POST':
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if email and password:
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    serializer = UserSerializer(user)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'Invalid password'})
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'})
        else:
            return Response({'error': 'Missing email or password'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'})
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)