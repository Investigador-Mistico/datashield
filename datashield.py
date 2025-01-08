import os
import time

# Função para exibir o banner
def show_banner():
    print("=" * 50)
    print(" " * 10 + "DataShield - Password Cracker")
    print("=" * 50)
    print("\n")

# Função para exibir o menu
def show_menu():
    print("[1] Ataque de Força Bruta")
    print("[2] Ataque com Wordlist")
    print("[3] Analisar Arquivo Protegido")
    print("[4] Sair")
    print("\n")

# Função para ataque de força bruta
def brute_force_attack(file_path):
    print("\n[!] Iniciando ataque de força bruta...")
    time.sleep(1)
    os.system(f"john --incremental {file_path}")
    print("[!] Ataque de força bruta concluído!\n")

# Função para ataque com wordlist
def wordlist_attack(file_path, wordlist_path):
    print("\n[!] Iniciando ataque com wordlist...")
    time.sleep(1)
    os.system(f"john --wordlist={wordlist_path} {file_path}")
    print("[!] Ataque com wordlist concluído!\n")

# Função para analisar arquivos protegidos
def analyze_file(file_path):
    print("\n[!] Analisando o arquivo...")
    time.sleep(1)
    os.system(f"zip2john {file_path} > hash.txt")
    print("[!] Análise concluída! Hash salvo em 'hash.txt'\n")

# Programa principal
def main():
    while True:
        show_banner()
        show_menu()
        choice = input("[?] Escolha uma opção: ")

        if choice == "1":
            file_path = input("[?] Caminho do arquivo protegido: ")
            brute_force_attack(file_path)
        elif choice == "2":
            file_path = input("[?] Caminho do arquivo protegido: ")
            wordlist_path = input("[?] Caminho da wordlist: ")
            wordlist_attack(file_path, wordlist_path)
        elif choice == "3":
            file_path = input("[?] Caminho do arquivo protegido: ")
            analyze_file(file_path)
        elif choice == "4":
            print("\n[!] Saindo do DataShield...")
            break
        else:
            print("[!] Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()

