#!/bin/bash

# Função para exibir o banner
banner() {
  clear
  echo "==================================="
  echo "          DataShield Painel        "
  echo "==================================="
}

# Função para a tela de login
login() {
  local user password
  echo -n "Usuário: "
  read user
  echo -n "Senha: "
  read -s password
  echo ""
  
  if [[ $user == "123" && $password == "123" ]]; then
    echo "Login bem-sucedido!"
    menu
  else
    echo "Usuário ou senha incorretos. Tente novamente."
    sleep 2
    banner
    login
  fi
}

# Função para o menu principal
menu() {
  while true; do
    clear
    banner
    echo "1. Atualizar Painel"
    echo "2. Sair"
    echo -n "Escolha uma opção: "
    read option

    case $option in
      1) update_painel ;;
      2) exit 0 ;;
      *) echo "Opção inválida. Tente novamente." ;;
    esac
    sleep 2
  done
}

# Função para atualizar o painel
update_painel() {
  echo "Atualizando painel..."
  apt update && apt upgrade -y
  echo "Atualização concluída!"
  sleep 2
}

# Início do programa
banner
login
