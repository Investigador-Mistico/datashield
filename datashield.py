#!/bin/bash

# Definições de cores para uma interface mais atraente
RED='\033[1;31m'
GREEN='\033[1;32m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
WHITE='\033[1;37m'
RESET='\033[0m'

# Função para exibir o banner estilizado
banner() {
  clear
  echo -e "${CYAN}"
  echo "==========================================================="
  echo "               ██████╗  █████╗ ███████╗██╗  ██╗            "
  echo "              ██╔═══██╗██╔══██╗██╔════╝██║  ██║            "
  echo "              ██║   ██║███████║█████╗  ███████║            "
  echo "              ██║   ██║██╔══██║██╔══╝  ██╔══██║            "
  echo "              ╚██████╔╝██║  ██║███████╗██║  ██║            "
  echo "               ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝            "
  echo "          DataShield - Painel Avançado de Segurança        "
  echo "==========================================================="
  echo -e "${RESET}"
}

# Função para a tela de login
login() {
  local user password
  echo -e "${WHITE}Usuário: ${RESET}"
  read user
  echo -e "${WHITE}Senha: ${RESET}"
  read -s password
  echo ""

  if [[ $user == "123" && $password == "123" ]]; then
    echo -e "${GREEN}Login bem-sucedido!${RESET}"
    sleep 1
    menu
  else
    echo -e "${RED}Usuário ou senha incorretos. Tente novamente.${RESET}"
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
    echo -e "${BLUE}1. Atualizar Painel${RESET}"
    echo -e "${BLUE}2. Consultar IP${RESET}"
    echo -e "${BLUE}3. Analisar URL (SQL Injection)${RESET}"
    echo -e "${BLUE}4. Sair${RESET}"
    echo -e "${CYAN}Escolha uma opção:${RESET}"
    read option

    case $option in
      1) update_painel ;;
      2) consultar_ip ;;
      3) analisar_url ;;
      4) exit 0 ;;
      *) echo -e "${RED}Opção inválida. Tente novamente.${RESET}" ;;
    esac
    sleep 2
  done
}

# Função para atualizar o painel usando o repositório GitHub
update_painel() {
  echo -e "${CYAN}Atualizando painel...${RESET}"
  if [[ ! -d "datashield" ]]; then
    echo -e "${WHITE}Clonando repositório...${RESET}"
    git clone https://github.com/Investigador-Mistico/datashield.git || {
      echo -e "${RED}Erro ao clonar repositório.${RESET}"
      return
    }
  else
    echo -e "${WHITE}Atualizando repositório existente...${RESET}"
    cd datashield || return
    git pull || {
      echo -e "${RED}Erro ao atualizar repositório.${RESET}"
      return
    }
    cd ..
  fi
  echo -e "${GREEN}Painel atualizado com sucesso!${RESET}"
  sleep 2
}

# Função para consultar informações de um IP
consultar_ip() {
  echo -e "${WHITE}Digite o IP para consulta:${RESET}"
  read ip
  echo -e "${CYAN}Consultando informações de IP...${RESET}"
  curl -s "http://ip-api.com/json/$ip" | jq || {
    echo -e "${RED}Erro ao buscar informações do IP. Certifique-se de estar conectado à internet.${RESET}"
  }
  sleep 3
}

# Função para analisar vulnerabilidades de SQL Injection em uma URL
analisar_url() {
  echo -e "${WHITE}Digite a URL para análise:${RESET}"
  read url
  echo -e "${CYAN}Verificando vulnerabilidades na URL usando SQLMap...${RESET}"

  # Verifica vulnerabilidades básicas de SQL Injection
  echo -e "${BLUE}Executando sqlmap para descobrir bancos de dados...${RESET}"
  sqlmap -u "$url" --batch --dbs

  echo -e "${CYAN}Deseja listar as tabelas de um banco específico? (s/n)${RESET}"
  read resposta
  if [[ $resposta == "s" || $resposta == "S" ]]; then
    echo -e "${WHITE}Digite o nome do banco de dados:${RESET}"
    read db_name
    sqlmap -u "$url" --batch -D "$db_name" --tables
  fi

  echo -e "${CYAN}Deseja consultar dados de uma tabela específica? (s/n)${RESET}"
  read resposta
  if [[ $resposta == "s" || $resposta == "S" ]]; then
    echo -e "${WHITE}Digite o nome da tabela:${RESET}"
    read table_name
    sqlmap -u "$url" --batch -D "$db_name" -T "$table_name" --dump
  fi

  echo -e "${GREEN}Análise concluída!${RESET}"
  sleep 3
}

# Início do programa
banner
login
