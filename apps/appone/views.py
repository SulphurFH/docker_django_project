from django.http import JsonResponse

# Create your views here.

def first_api_view(request):
    context = {
                'name': 'docker_django_project',
                'version': '0.1v',
                'use': 'test',
                'test_one': 'add response,test git pull',
                'test_two': 'test container git pull'
            }
    return JsonResponse(context)
