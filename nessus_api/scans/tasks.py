from celery import shared_task
import docker
from .models import ScanRequest

@shared_task
def start_scan_task(scan_request_id, ip_chunks):
    client = docker.from_env()
    scan_request = ScanRequest.objects.get(id=scan_request_id)
    
    try:
        # Nessus taraması için yeni bir Docker container başlatıyoruz
        container = client.containers.run(
            "tenableio/nessus",  # Nessus tarama için kullanılan image adı
            command=f"nessuscli scan --targets {','.join(ip_chunks)}",  # IP'leri taratıyoruz
            detach=True
        )
        
        container.wait()  # Tarama tamamlanana kadar bekliyoruz
        result = container.logs().decode('utf-8')  # Tarama sonuçlarını alıyoruz

        # Sonuçları modelde güncelliyoruz
        scan_request.result = result
        scan_request.status = 'completed'

        # Tarama tamamlandığında container'ı siliyoruz
        container.remove()
        
    except Exception as e:
        scan_request.status = 'failed'
        scan_request.result = str(e)
    finally:
        scan_request.save()
