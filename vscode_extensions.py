import subprocess

def install_vscode_extensions(extensions):
    for extension in extensions:
        try:
            subprocess.run(["code", "--install-extension", extension])
        except Exception as e:
            print(f"Error al instalar la extensión {extension}: {str(e)}")

if __name__ == "__main__":
    from setup import vs_extensions

    install_vscode_extensions(vs_extensions)
