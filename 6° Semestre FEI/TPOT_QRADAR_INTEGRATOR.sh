#!/bin/bash

# Definir cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # Sem cor

# Instala o plugin logstash-output-syslog após cada reinicialização da instância do TPOT
function create_logstash_sh() {
	sudo cat << EOF | sudo tee /opt/tpot/logstash_syslog.sh > /dev/null
# Script made to install logstash-output-syslog plugin after every restart of TPOT instance.
# Created by João Pedro Rosa Cezarino
# Date: 14/12/2022
# T-Systems Security Team

echo -e "\033[01;32m[!] Installing logstash-output-syslog plugin_version... [!]\033[0m"
sudo docker exec -u 0 logstash /usr/share/logstash/bin/logstash-plugin install logstash-output-syslog
plugin_version=\$(sudo docker exec -u 0 logstash /usr/share/logstash/bin/logstash-plugin list --verbose | grep 'logstash-output-syslog' | cut -d "(" -f 2 | cut -d ")" -f 1)
sleep 4

echo -e "\033[01;32m[!] Changing permissions to user logstash... [!]\033[0m"
sudo docker exec -u 0 logstash chown -R logstash:logstash /usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-output-syslog-\$plugin_version
sudo docker exec -u 0 logstash chmod 755 /usr/share/logstash/vendor/bundle/jruby/2.6.0/gems/logstash-output-syslog-\$plugin_version
sleep 2

echo -e "\033[01;32m[!] Restarting logstash container... [!]\033[0m"
sudo docker stop logstash
sleep 2
sudo docker start logstash

echo -e "\033[01;32m[!] DONE [!]\033[0m"
exit 0
EOF
}

function start_tpot(){
  sudo systemctl start tpot
  sleep 2
}

function stop_tpot(){
  sudo systemctl stop tpot
  sleep 2
}

# Muda a permissão do script logstash_syslog.sh
function change_script_permission() {
  sudo chmod +x /opt/tpot/logstash_syslog.sh
  sudo chown root:root /opt/tpot/logstash_syslog.sh
}

# Cria os arquivos de serviço logstash_output.service e logstash__output.timer
function create_service_files() {
  # Cria o arquivo de serviço logstash_output.service
  sudo cat << EOF | sudo tee /etc/systemd/system/logstash_output.service > /dev/null
[Unit]
Description=Execute the logstash-output-syslog installation on logstash docker container. 

[Service]
User=root
ExecStart=/bin/bash /opt/tpot/logstash_syslog.sh

[Install]
WantedBy=multi-user.target
EOF

  # Cria o arquivo de timer logstash_output.timer
  sudo cat << EOF | sudo tee /etc/systemd/system/logstash_output.timer > /dev/null
[Unit]
Description=Timer to run /opt/tpot/logstash_syslog.sh

[Timer]
Unit=logstash_output.service
OnBootSec=3min

[Install]
WantedBy=timers.target
EOF
}

# Ativa o timer de serviço logstash_output.timer
function enable_service_timer() {
  sudo systemctl enable logstash_output.timer
}

# Recarrega o daemon do sistema
function reload_system_daemon() {
  sudo systemctl daemon-reload
}

# Inicia o timer de serviço logstash_output.timer
function start_service_timer() {
  sudo systemctl start logstash_output.timer
}

#Reconfigure logstash.conf to transmit data to other destination
function edit_logstash_conf() {
  sudo docker exec -u 0 logstash cp /etc/logstash/logstash.conf /data/elk/logstash.conf
  stop_tpot
  echo -e "${RED}[!] T-POT Desligado [!]${NC}"
  read -p "[+] Entre com o endereço IP do seu SIEM: " answer
  if [[ ! $answer =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
	echo "${RED}[!] Endereço IP inválido - Encerrando o script... [+]${NC}"
	exit 0
  else
    sudo sed -i 's/\#if \[type\] == \"Suricata\" {/syslog {\
      host => \"\$answer\"\
      port => \"514\"\
      protocol => \"tcp\"\
      codec => json\
    } \
    #stdout {} \
    #if [type] == \"Suricata\" {/' /data/elk/logstash.conf
  fi
}

function set_logstash_conf_permissions(){
  sudo chmod 760 /data/elk/logstash.conf
  sudo chown tpot:tpot /data/elk/logstash.conf
}

function edit_tpot_yml(){
sudo sed -i '/image: "dtagdevsec\/logstash:2204"/a\
    volumes:\
    - \/data:\/data\
    - \/data\/elk\/logstash.conf:\/etc\/logstash\/logstash.conf' /opt/tpot/etc/tpot.yml
sudo awk '/- \/data\/elk\/logstash.conf:\/etc\/logstash\/logstash.conf/ {print; getline; getline; next} 1' /opt/tpot/etc/tpot.yml > /opt/tpot/etc/tpot_tmp.yml && sudo mv /opt/tpot/etc/tpot_tmp.yml /opt/tpot/etc/tpot.yml
}

function reboot_server() {
    read -p "Deseja reiniciar o servidor agora? (s/n): " answer
    if [ "$answer" = "s" ] || [ "$answer" = "S" ]; then
        echo -e "${RED}[!] Reiniciando o servidor [!]${NC}"
        sudo reboot
    else
        echo -e "${GREEN}[!] Encerrando o script [!]${NC}"
        exit 0
    fi
}

# Executa todas as funções em sequência
function main() {
  edit_logstash_conf
  echo -e "${GREEN}[!] Arquivo de configuração do Logstash atualizado com sucesso! [!]${NC}"
  set_logstash_conf_permissions
  echo -e "${GREEN}[!] Permissões do logstash.conf Alteradas [!]${NC}"
  edit_tpot_yml
  echo -e "${GREEN}[!] Configurações do TPOT.yml Alteradas [!]${NC}"
  start_tpot
  sleep 5
  echo -e "${GREEN}[!] T-POT Iniciado novamente [!]${NC}"
  create_logstash_sh
  echo -e "${GREEN}[!] Arquivo logstash_syslog criado [!]${NC}"
  change_script_permission
  echo -e "${GREEN}[!] Permissões do logstash_syslog Alteradas [!]${NC}"
  create_service_files
  echo -e "${GREEN}[!] Arquivos logstash_output.service e logstash__output.timer criados [!]${NC}"
  enable_service_timer
  echo -e "${GREEN}[!] logstash__output.timer ativado [!]${NC}"
  reload_system_daemon
  echo -e "${GREEN}[!] Daemon Recarregado [!]${NC}"
  start_service_timer
  echo -e "${GREEN}[!] Timer iniciado [!]${NC}"
  echo -e "${GREEN}[!] Todas as operações foram concluídas [!]${NC}"
  reboot_server
}

main