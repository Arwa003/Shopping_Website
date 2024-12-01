from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin Dashboard
    path('', include('website.urls')),        # Public Website
    path('dashboard/', include('dashboard.urls')), 
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
 # Dashboard routes
]
