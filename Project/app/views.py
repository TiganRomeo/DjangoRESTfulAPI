from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


@csrf_exempt
def AuthAPI(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'error': 'Invalid Credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Method "GET" not allowed.'}, status=405)


@csrf_exempt
def UserAddAPI(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        staff_status = request.POST.get('staff_status')
        if staff_status == 'true':
            staff_status = True
        elif staff_status == 'false':
            staff_status = False
        else:
            return JsonResponse({'error': 'Invalid staff status value'}, status=400)
        try:
            User.objects.create_user(username=username, email=email, password='password', first_name=first_name,
                                     last_name=last_name, is_staff=staff_status)
            return JsonResponse({'status': 'success'})
        except:
            return JsonResponse({'error': 'Failed to add user'}, status=500)
    else:
        return JsonResponse({'error': 'Method "GET" not allowed.'}, status=405)


@csrf_exempt
def UserListAPI(request):
    if request.method == 'GET':
        users = User.objects.all().values()
        return JsonResponse({'users': list(users)})
    else:
        return JsonResponse({'error': 'Method "POST" not allowed.'}, status=405)


@csrf_exempt
def UserEditAPI(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        staff_status = request.POST.get('staff_status')
        if staff_status == 'true':
            staff_status = True
        elif staff_status == 'false':
            staff_status = False
        else:
            return JsonResponse({'error': 'Invalid staff status value'}, status=400)
        try:
            user = User.objects.get(id=user_id)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.is_staff = staff_status
            user.save()
            return JsonResponse({'status': 'success'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except:
            return JsonResponse({'error': 'Failed to edit user'}, status=500)
    else:
        return JsonResponse({'error': 'Method "GET" not allowed.'}, status=405)