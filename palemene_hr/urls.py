from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),  # This includes the chatbot app's URLs
    path('', include('chatbot.urls')),  # Add this line to route the root URL to chatbot's URL
]
