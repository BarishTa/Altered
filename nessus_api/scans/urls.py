from django.urls import path
from . import views  # views dosyasını içe aktarıyoruz

urlpatterns = [
    path('', views.index, name='index'),  # Anasayfa
    path('start_scan/', views.start_scan, name='start_scan'),  # Tarama başlatma
    path('get_scan_results/', views.get_scan_results, name='get_scan_results'),  # Sonuçları alma
]
