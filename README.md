-----

````markdown
# ❄️ EcoFreeze IoT: Monitoreo de Cámaras Frías

Sistema de monitoreo en tiempo real para cámaras de refrigeración industrial, utilizando un **ESP32** (simulado), un sensor **DHT22** y un backend robusto en **Django**. 

Este proyecto resuelve el problema de la latencia en simuladores mediante una arquitectura de túneles híbridos.

## 🚀 Características Principales
* **Monitoreo en Tiempo Real**: Ingesta de datos de temperatura y humedad cada 5 segundos.
* **Alertas Críticas**: Sistema visual que detecta temperaturas superiores a los **-15°C** (Riesgo de merma).
* **Dashboard Dinámico**: Interfaz web moderna con Bootstrap y actualización automática vía AJAX/Fetch.
* **Arquitectura Híbrida**: 
    - **Backend**: Django 6.0 + SQLite.
    - **Simulación**: Wokwi dentro de VS Code.
    - **Túnel de Acceso**: Ngrok para visualización remota.

## 🛠️ Stack Tecnológico
* **C++ / Arduino**: Código para el firmware del ESP32.
* **Python / Django**: Servidor web y API REST.
* **HTML/JS/Bootstrap**: Frontend del Dashboard.
* **PlatformIO**: Entorno de desarrollo para el hardware.

## 📋 Requisitos e Instalación

### 1. Backend (Django)
```bash
# Clonar el repositorio
git clone <tu-url-de-github>

# Instalar dependencias
pip install django django-cors-headers

# Correr migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
````

### 2\. Simulación (ESP32)

1.  Abrir la carpeta del proyecto en **VS Code**.
2.  Asegurarse de tener instalada la extensión de **Wokwi**.
3.  Compilar y subir el código usando **PlatformIO**.
4.  El simulador se conectará automáticamente a la API interna mediante `host.wokwi.internal`.

## 🌐 Acceso Remoto (Ngrok)

Para permitir que usuarios externos vean el Dashboard sin afectar la estabilidad del simulador, se utiliza un túnel de Ngrok:

```bash
ngrok http 8000
```

*Cualquier persona con el link generado podrá monitorear la cámara fría en tiempo real.*

## ⚠️ Lógica de Negocio (Alerta de Seguridad)

El sistema aplica una regla de criticidad estricta:

  * **Estado Óptimo**: Temperatura \<= -15.00 °C.
  * **Estado de Peligro**: Temperatura \> -15.00 °C.
  * *Nota: Los datos se redondean automáticamente a 2 decimales para mayor precisión técnica.*

## 📝 Autor

  * **Inmer** - *Desarrollo Integral*

<!-- end list -->

```

---
