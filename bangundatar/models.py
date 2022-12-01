from django.db import models

# Create your models here.

class MateriMatematika(models.Model):
    nomor = models.CharField(max_length=300, null=True)
    nama = models.CharField(max_length=100)
    foto = models.CharField(max_length=300, null=True)

    def _str_(self):
        return "{}".format(self.nama)