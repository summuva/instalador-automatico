# Instalador de Visual Studio Code y paquetes para Python

Este script de Python te permite verificar si Visual Studio Code está instalado en tu sistema y, si no lo está, lo instalará automáticamente en sistemas Linux. Además, el script desactiva temporalmente IPv6 en sistemas Unix/Linux, instala extensiones de Visual Studio Code y actualiza el índice de paquetes, instala pip para Python 3 y algunos paquetes de Python necesarios.

## Requisitos previos

Antes de ejecutar este script, asegúrate de que:

- Estás ejecutando el script en un sistema Unix/Linux (Linux o macOS).
- Tienes permisos de administrador (sudo) para instalar paquetes y extensiones.
- Tienes Python 3 en tu sistema.

## Uso

1. Abre una terminal en tu sistema Unix/Linux.

2. Clona este repositorio o descarga el archivo Python (`instalador.py`) en tu sistema.

3. Ejecuta el script Python utilizando el siguiente comando:

   $python3 instalador.py

# Notas importantes
- Este script solo es compatible con sistemas Unix/Linux (Linux o macOS).

- Asegúrate de tener una conexión a Internet activa para descargar Visual Studio Code y las extensiones.

- Puedes personalizar la lista de extensiones de Visual Studio Code que deseas instalar editando la variable extensions en el script.

- Puedes agregar los nombres de paquetes de Python adicionales que deseas instalar en la lista packages.

- El script desactiva temporalmente IPv6 en sistemas Unix/Linux ya que en la mayoria de dispositivos probados tendia a errores al momento de instalar las extensiones.

## Contribuciones
Si deseas contribuir a este proyecto, ¡siéntete libre de hacerlo! Puedes abrir problemas (issues) o enviar solicitudes de extracción (pull requests) en el repositorio.

##Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.