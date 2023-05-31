from django.db import models

# Create your models here.
class Pdaftar(models.Model):
    nama=models.CharField(max_length=50)
    alamat=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.nama