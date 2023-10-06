import subprocess
import platform
import os
import requests

def check_vscode_installed():
    '''Retorna un true o un false dependiendo de la existencia de vscode en el sistema'''
    check_installed_command = "code --version"
    try:
        subprocess.run(check_installed_command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def download_vscode_deb(download_url, download_path):
    '''
    Recibe como primer parametro la url del paquete.deb que queremos instalar
    Como segundo parametro recibe el path de donde queremos guardar el archivo.
    De haber algun error, devuelve False
    '''
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        with open(download_path, "wb") as file:
            file.write(response.content)
        return True
    except Exception as e:
        print(f"Error al descargar el archivo .deb de Visual Studio Code: {str(e)}")
        return False

def install_vscode_deb(download_path):
    '''Instala el archivo.deb'''
    install_command = f"sudo dpkg -i {download_path}"
    try:
        subprocess.run(install_command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar Visual Studio Code: {str(e)}")
        return False

def main():
    if check_vscode_installed():
        print("Visual Studio Code ya está instalado en tu sistema.")
    else:
        print("Visual Studio Code no está instalado. Se procederá a la instalación.")
        download_url = "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64"
        download_path = "/tmp/vscode.deb"
        # un proceso va encima del otro ya que los validadores condicionaran las acciones
        if download_vscode_deb(download_url, download_path):
            if install_vscode_deb(download_path):
                os.remove(download_path)
                print("Visual Studio Code se ha instalado correctamente.")
            else:
                print("Error al instalar Visual Studio Code.")
                exit(1)
        else:
            exit(1)

if __name__ == "__main__":
    main()
