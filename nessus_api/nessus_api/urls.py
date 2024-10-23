# nessus_api/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scans/', include('scans.urls')),
    path('', RedirectView.as_view(url='scans/', permanent=False)),  # Boş yolu scans/ ile yönlendir
]
