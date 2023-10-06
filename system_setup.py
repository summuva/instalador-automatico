import subprocess
import platform

def disable_ipv6():
    if platform.system() == 'Linux' or platform.system() == 'Darwin':
        try:
            subprocess.run(["sudo", "sysctl", "-w", "net.ipv6.conf.all.disable_ipv6=1"])
            subprocess.run(["sudo", "sysctl", "-w", "net.ipv6.conf.default.disable_ipv6=1"])
        except Exception as e:
            print(f"Error al desactivar IPv6: {str(e)}")

def update_package_index():
    update_command = "sudo apt update"
    try:
        subprocess.run(update_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al actualizar el índice de paquetes: {str(e)}")
        exit(1)

def install_pip_for_python3():
    install_command = "sudo apt install python3-pip -y"
    try:
        subprocess.run(install_command, shell=True, check=True)
        print("pip se ha instalado correctamente para Python 3.")
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar pip para Python 3: {str(e)}")
        exit(1)

def verify_pip_version():
    try:
        version_command = "pip3 --version"
        subprocess.run(version_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al verificar la versión de pip: {str(e)}")
        exit(1)

if __name__ == "__main__":
    disable_ipv6()
    update_package_index()
    install_pip_for_python3()
    verify_pip_version()
