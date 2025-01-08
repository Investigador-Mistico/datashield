import os
import time

# Cores para a interface
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Função para exibir o banner
def show_banner():
    os.system("clear")
    print(f"{Colors.OKCYAN}" + "=" * 60)
    print(f"{Colors.OKCYAN}{Colors.BOLD}" + " " * 16 + "██████╗  █████╗ ████████╗ █████╗ ")
    print(f"{Colors.OKCYAN}{Colors.BOLD}" + " " * 16 + "██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗")
    print(f"{Colors.OKCYAN}{Colors.BOLD}" + " " * 16 + "██████╔╝███████║   ██║   ███████║")
    print(f"{Colors.OKCYAN}{Colors.BOLD}" + " " * 16 + "██╔═══╝ ██╔══██║   ██║   ██╔══██║")
    print(f"{Colors.OKCYAN}{Colors.BOLD}" + " " * 16 + "██║     ██║  ██║   ██║   ██║  ██║")
    print(f"{Colors.OKCYAN}{Colors.BOLD}" + " " * 16 + "╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝")
    print(f"{Colors.OKGREEN}{Colors.BOLD}" + " " * 17 + "DataShield - Password Cracker")
    print(f"{Colors.OKCYAN}" + "=" * 60 + Colors.ENDC)
    print("\n")

# Função para exibir o menu
def show_menu():
    print(f"{Colors.OKGREEN}[1] Quebrar senha com força bruta")
    print(f"{Colors.OKGREEN}[2] Quebrar senha com wordlist")
    print(f"{Colors.OKGREEN}[3] Analisar arquivo protegido")
    print(f"{Colors.OKGREEN}[4] Sair{Colors.ENDC}")
    print("\n")

# Função para quebrar senha com força bruta
def brute_force_attack(file_path):
    print(f"{Colors.WARNING}\n[!] Iniciando ataque de força bruta...{Colors.ENDC}")
    time.sleep(1)
    os.system(f"john --incremental {file_path}")
    print(f"{Colors.OKGREEN}[!] Ataque de força bruta concluído!{Colors.ENDC}")
    print(f"{Colors.OKCYAN}[!] Resultados encontrados:{Colors.ENDC}")
    os.system("john --show {0}".format(file_path))

# Função para quebrar senha com wordlist
def wordlist_attack(file_path, wordlist_path):
    print(f"{Colors.WARNING}\n[!] Iniciando ataque com wordlist...{Colors.ENDC}")
    time.sleep(1)
    os.system(f"john --wordlist={wordlist_path} {file_path}")
    print(f"{Colors.OKGREEN}[!] Ataque com wordlist concluído!{Colors.ENDC}")
    print(f"{Colors.OKCYAN}[!] Resultados encontrados:{Colors.ENDC}")
    os.system("john --show {0}".format(file_path))

# Função para analisar arquivos protegidos
def analyze_file(file_path):
    print(f"{Colors.WARNING}\n[!] Analisando o arquivo...{Colors.ENDC}")
    time.sleep(1)
    os.system(f"zip2john {file_path} > hash.txt")
    print(f"{Colors.OKGREEN}[!] Análise concluída! Hash salvo em 'hash.txt'{Colors.ENDC}")

# Programa principal
def main():
    while True:
        show_banner()
        show_menu()
        choice = input(f"{Colors.OKBLUE}[?] Escolha uma opção: {Colors.ENDC}")

        if choice == "1":
            file_path = input(f"{Colors.OKCYAN}[?] Caminho do arquivo protegido: {Colors.ENDC}")
            brute_force_attack(file_path)
            input(f"{Colors.OKGREEN}[!] Pressione Enter para continuar...{Colors.ENDC}")
        elif choice == "2":
            file_path = input(f"{Colors.OKCYAN}[?] Caminho do arquivo protegido: {Colors.ENDC}")
            wordlist_path = input(f"{Colors.OKCYAN}[?] Caminho da wordlist: {Colors.ENDC}")
            wordlist_attack(file_path, wordlist_path)
            input(f"{Colors.OKGREEN}[!] Pressione Enter para continuar...{Colors.ENDC}")
        elif choice == "3":
            file_path = input(f"{Colors.OKCYAN}[?] Caminho do arquivo protegido: {Colors.ENDC}")
            analyze_file(file_path)
            input(f"{Colors.OKGREEN}[!] Pressione Enter para continuar...{Colors.ENDC}")
        elif choice == "4":
            print(f"{Colors.FAIL}\n[!] Saindo do DataShield...{Colors.ENDC}")
            break
        else:
            print(f"{Colors.FAIL}[!] Opção inválida! Tente novamente.{Colors.ENDC}")

if __name__ == "__main__":
    main()

