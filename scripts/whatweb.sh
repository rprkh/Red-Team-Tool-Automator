#!/bin/bash

echo "Check if the user has sudo privileges"
if [ $(id -u) -ne 0 ]; then
  echo "This script requires sudo privileges. Please run with sudo."
  exit 1
fi

echo "Detecting Linux distribution"

if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
elif type lsb_release >/dev/null 2>&1; then
    OS=$(lsb_release -si)
elif [ -f /etc/lsb-release ]; then
    . /etc/lsb-release
    OS=$DISTRIB_ID
elif [ -f /etc/debian_version ]; then
    OS=debian
elif [ -f /etc/fedora-release ]; then
    OS=fedora
elif [ -f /etc/redhat-release ]; then
    if grep -q "CentOS" /etc/redhat-release; then
        OS=centos
    else
        OS=rhel
    fi
else
    OS=$(uname -s)
fi

if [[ "$OS" == "ubuntu" || "$OS" == "debian" || "$OS" == "kali" ]]; then
  apt install -y whatweb
elif [[ "$OS" == "arch" || "$OS" == "rhel" || "$OS" == "centos" || "$OS" == "fedora"]]; then
  git clone https://github.com/urbanadventurer/WhatWeb.git 
  cd WhatWeb
  ./whatweb 
else 
  echo "Unsupported Linux distribution: $OS"
fi

echo "WhatWeb installed successfully."

