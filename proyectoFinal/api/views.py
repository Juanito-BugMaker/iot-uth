from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SensorData

@csrf_exempt # Desactiva seguridad CSRF solo para que el ESP32 pueda enviar datos fácil
def recibir_datos(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            temp = data.get('temperatura')
            hum = data.get('humedad')
            
            # 1. Qué está mandando realmente el ESP32
            print(f"Datos recibidos -> Temp: {temp}, Hum: {hum}")
            
            # Guardar en base de datos
            nuevo_registro = SensorData.objects.create(temperatura=temp, humedad=hum)
            
            # 2. Confirmación de guardado
            print("Registro guardado exitosamente en la BD.")
            
            return JsonResponse({'status': 'success', 'message': 'Datos guardados correctamente'})
        
        except Exception as e:
            # 3. ¡Si hay error, que la terminal grite y devuelva un 400 real!
            print(f"ERROR AL GUARDAR: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    return JsonResponse({'status': 'invalid method'})

def dashboard(request):
    """Renderiza la página principal del dashboard."""
    return render(request, 'api/dashboard.html')

def obtener_datos(request):
    """Devuelve los últimos 10 registros en formato JSON para la tabla en tiempo real."""
    # Traemos los últimos 10 registros ordenados del más nuevo al más viejo
    ultimos_datos = SensorData.objects.all().order_by('-fecha_registro')[:10]
    
    data_list = []
    for dato in ultimos_datos:
        data_list.append({
            'id': dato.id,
            'temperatura': dato.temperatura,
            'humedad': dato.humedad,
            # Formateamos la fecha para que se vea bonita
            'fecha': dato.fecha_registro.strftime('%d/%m/%Y %H:%M:%S')
        })
        
    return JsonResponse({'datos': data_list})