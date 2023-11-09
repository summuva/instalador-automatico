import subprocess
import platform
import os
import requests

# Comando para verificar si Visual Studio Code ya está instalado
check_installed_command = "code --version"

try:
    # Intentar ejecutar el comando para verificar si ya está instalado
    subprocess.run(check_installed_command, shell=True, check=True)
    print("Visual Studio Code ya está instalado en tu sistema.")
except subprocess.CalledProcessError as e:
    print("Visual Studio Code no está instalado. Se procederá a la instalación.")

    # URL de descarga del archivo .deb de Visual Studio Code
    download_url = "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"

    # Ruta donde se guardará el archivo .deb descargado
    download_path = "/tmp/vscode.deb"

    # Descargar el archivo .deb desde la URL
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        with open(download_path, "wb") as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error al descargar el archivo .deb de Visual Studio Code: {str(e)}")
        exit(1)

    # Instalar el archivo .deb
    install_command = f"sudo dpkg -i {download_path}"
    try:
        subprocess.run(install_command, shell=True, check=True)
        print("Visual Studio Code se ha instalado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar Visual Studio Code: {str(e)}")
        exit(1)

    # Limpiar el archivo .deb descargado
    os.remove(download_path)

print("Instalación de Visual Studio Code completada.")






# Verificar si el sistema es Unix/Linux (Linux o macOS)
if platform.system() == 'Linux' or platform.system() == 'Darwin':
    try:
        # Desactivar IPv6 temporalmente
        subprocess.run(["sudo", "sysctl", "-w", "net.ipv6.conf.all.disable_ipv6=1"])
        subprocess.run(["sudo", "sysctl", "-w", "net.ipv6.conf.default.disable_ipv6=1"])






        # Instalar extensiones de Visual Studio Code
        extensions = [
            "ms-toolsai.jupyter",
            "ms-python.vscode-pylance",
            # Agrega aquí los nombres de las extensiones que deseas instalar
        ]







        for extension in extensions:
            try:
                subprocess.run(["code", "--install-extension", extension])
            except Exception as e:
                print(f"Error al instalar la extensión {extension}: {str(e)}")

        print("Instalación completada.")
    except Exception as e:
        print(f"Error al desactivar IPv6 o al instalar extensiones: {str(e)}")
else:
    print("Este script solo es compatible con sistemas Unix/Linux (Linux o macOS).")







# Actualiza el índice de paquetes
update_command = "sudo apt update"
try:
    subprocess.run(update_command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error al actualizar el índice de paquetes: {str(e)}")
    exit(1)

# Instala pip para Python 3
install_command = "sudo apt install python3-pip -y"
try:
    subprocess.run(install_command, shell=True, check=True)
    print("pip se ha instalado correctamente para Python 3.")
except subprocess.CalledProcessError as e:
    print(f"Error al instalar pip para Python 3: {str(e)}")
    exit(1)

# Verifica la versión de pip instalada
try:
    version_command = "pip3 --version"
    subprocess.run(version_command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error al verificar la versión de pip: {str(e)}")
    exit(1)

print("Instalación de pip completada.")




# Instalar Paquetes 
# Agregar los nombres de los paquetes a la lista de packages
packages = ["ipykernel","venv"]
for package in packages:
    try:
        paquete = f"python3-{package}"
        subprocess.run(["sudo", "apt", "install",paquete])
    except Exception as e:
        for i in range(10):
            print(f"Error al instalar ipykernel: {str(e)}")
