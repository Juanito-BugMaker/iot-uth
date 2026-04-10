from django.db import models

# Create your models here.

# from django.db import models

class SensorData(models.Model):
    temperatura = models.FloatField()
    humedad = models.FloatField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temp: {self.temperatura}°C, Hum: {self.humedad}%"