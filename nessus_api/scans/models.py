from django.db import models

class ScanRequest(models.Model):
    ip_list = models.TextField()  # Kullanıcının girdiği IP listesi
    status = models.CharField(max_length=20, default='pending')  # Tarama durumu (pending, completed, failed)
    result = models.JSONField(null=True, blank=True)  # Tarama sonuçları (JSON formatında)
    
    def __str__(self):
        return f"Tarama - {self.id} - Durum: {self.status}"
