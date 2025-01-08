import os
import pyfiglet
import zipfile
import subprocess
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS


# Função para exibir o banner
def show_banner():
    banner = pyfiglet.figlet_format("DataShield")
    print(banner)
    print("=" * 50)
    print("1. Quebra de senha de arquivo ZIP")
    print("2. Análise de metadados")
    print("3. Sair")
    print("=" * 50)


# Função para quebra de senha de arquivo ZIP
def quebra_senha_zip():
    zip_file = input("\nDigite o caminho do arquivo ZIP: ")
    wordlist = input("Digite o caminho da wordlist (ex: rockyou.txt): ")

    if not os.path.exists(zip_file):
        print("Arquivo ZIP não encontrado!")
        return

    if not os.path.exists(wordlist):
        print("Wordlist não encontrada!")
        return

    with zipfile.ZipFile(zip_file, 'r') as zf:
        with open(wordlist, 'r', encoding='latin-1') as wl:
            for word in wl:
                password = word.strip()
                try:
                    zf.extractall(pwd=password.encode('utf-8'))
                    print(f"\nSenha encontrada: {password}")
                    return
                except Exception:
                    pass
    print("Senha não encontrada na wordlist.")


# Função para análise de metadados
def analise_metadados():
    arquivo = input("\nDigite o caminho do arquivo (imagem, PDF, etc.): ")

    if not os.path.exists(arquivo):
        print("Arquivo não encontrado!")
        return

    print("\nMetadados encontrados:")
    if arquivo.lower().endswith(('.jpg', '.jpeg', '.png')):
        try:
            image = Image.open(arquivo)
            exif_data = image._getexif()
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag_name = TAGS.get(tag_id, tag_id)
                    print(f"{tag_name}: {value}")
            else:
                print("Nenhum metadado encontrado.")
        except Exception as e:
            print(f"Erro ao ler metadados: {e}")
    else:
        try:
            result = subprocess.check_output(['exiftool', arquivo])
            print(result.decode())
        except FileNotFoundError:
            print("exiftool não encontrado. Instale com: sudo apt install exiftool")
        except Exception as e:
            print(f"Erro ao analisar o arquivo: {e}")


# Menu principal
def main():
    while True:
        show_banner()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            quebra_senha_zip()
        elif choice == "2":
            analise_metadados()
        elif choice == "3":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
