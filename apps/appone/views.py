from django.http import JsonResponse

# Create your views here.

def first_api_view(request):
    context = {
                'name': 'docker_django_project',
                'version': '0.1v',
                'use': 'test',
                'use2': 'test2',
            }
    return JsonResponse(context)
