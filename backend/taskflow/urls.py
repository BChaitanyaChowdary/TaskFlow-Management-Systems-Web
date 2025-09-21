"""
URL configuration for taskflow project.
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static

def root_view(_request):
    return JsonResponse({
        'message': 'TaskFlow API',
        'api_base': '/api/',
        'endpoints': [
            '/api/auth/',
            '/api/tasks/',
            '/api/projects/',
            '/admin/'
        ]
    })


urlpatterns = [
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/projects/', include('projects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
