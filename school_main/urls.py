from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student.urls')),  # Map the base URL to the student app
    path('api/', include('student.api_urls')),  # Map API endpoints to the student app's API URLs
    path('student/', include('student.urls')),


    # Front end URLs
    
]
