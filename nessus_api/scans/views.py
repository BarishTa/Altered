from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScanRequest
from .tasks import start_scan_task

@api_view(['GET'])
def start_scan(request):
    # Kullanıcının girdiği IP listesini al
    ip_list = request.data.get('ip_list', '')
    
    # IP'leri maksimum 16'lı gruplara bölüyoruz
    ip_chunks = [ip_list.split()[i:i + 16] for i in range(0, len(ip_list.split()), 16)]

    # ScanRequest modelinde yeni bir tarama isteği oluştur
    scan_request = ScanRequest.objects.create(ip_list=ip_list)

    # Celery görevini başlat (asenkron olarak Nessus taramasını başlatacak)
    for chunk in ip_chunks:
        start_scan_task.delay(scan_request.id, chunk)

    return Response({'status': 'Tarama başlatıldı', 'scan_id': scan_request.id})

@api_view(['GET'])
def get_scan_results(request):
    # Tüm tarama isteklerini ve sonuçlarını döndürüyoruz
    scan_requests = ScanRequest.objects.all().values('id', 'ip_list', 'status', 'result')
    return Response({'results': list(scan_requests)})

@api_view(['GET'])
def index(request):
    return Response({'message': 'Tarama başlatmak için /scans/start_scan/ veya sonuçları görüntülemek için /scans/get_scan_results/ kullanabilirsiniz.'})
