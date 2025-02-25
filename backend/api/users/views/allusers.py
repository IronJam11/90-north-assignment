from django.http import JsonResponse
from django.core.files.storage import default_storage
from api.models import User
from rest_framework.response import Response  # type: ignore
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        auth_header = request.headers.get('Authorization')

        if auth_header is None or not auth_header.startswith('Bearer '):
            return JsonResponse({"error": "Token not provided or incorrect format"}, status=status.HTTP_400_BAD_REQUEST)
        users = User.objects.all() 
        user_details = []
        print(users)

        for user in users: 
            profile_picture_url = default_storage.url(user.profile_picture.name) if user.profile_picture else None
            if profile_picture_url == "": 
                 profile_picture_url = None
            user_details.append({
                'id': user.id,
                'name':user.name,
                'username':user.username,
                'email':user.email,
                'bio':user.bio,
                'date_joined':user.date_joined,
                'profile_picture': profile_picture_url
            })
        return JsonResponse({'users': user_details}, safe=False)

from django.http import JsonResponse
from django.db.models import Q

def search_users(request):
    if request.method == 'GET':
        search_query = request.GET.get('query', '')

        users = User.objects.filter(
            Q(username__icontains=search_query) |
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query)
        ).distinct()

        user_details_set = set() 
        user_details = []

        for user in users:
            
                profile_picture_url = default_storage.url(user.profile_picture.name) if user.profile_picture else ""
                details = {
                    'id': user.id,
                    'name':user.name,
                    'username':user.username,
                    'email':user.email,
                    'bio':user.bio,
                    'date_joined':user.date_joined,
                    'name':user.name,
                    'profile_picture': profile_picture_url
                    
                }
                
                # Add to set to ensure uniqueness
                if user.username not in user_details_set:
                    user_details.append(details)
                    user_details_set.add(user.username)

        return JsonResponse({'users': user_details}, safe=False)
