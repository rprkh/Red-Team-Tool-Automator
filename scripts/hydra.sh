#!/bin/bash

# Check if the script is being run with sudo
if [[ $EUID -ne 0 ]]; then
  echo "Please run this script with sudo."
  exit 1
fi

# Detect Linux distribution
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
elif type lsb_release >/dev/null 2>&1; then
    OS=$(lsb_release -si | tr '[:upper:]' '[:lower:]')
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
    OS=$(uname -s | tr '[:upper:]' '[:lower:]')
fi

# Install Hydra and SecLists based on the distribution
case $OS in
    ubuntu|debian|kali)
        apt-get update || { echo "Failed to update apt cache. Please check your internet connection or try again later."; exit 1; }
        apt-get install -y hydra seclists || { echo "Failed to install Hydra or SecLists. Please try again."; exit 1; }
        ;;
    centos|rhel|fedora)
        yum install -y hydra epel-release || { echo "Failed to install Hydra or EPEL release. Please try again."; exit 1; }
        yum install -y seclists || { echo "Failed to install SecLists. Please try again."; exit 1; }
        ;;
    arch)
        pacman -Sy --noconfirm hydra seclists || { echo "Failed to install Hydra or SecLists. Please try again."; exit 1; }
        ;;
    *)
        echo "Unsupported Linux distribution: $OS"
        exit 1
        ;;
esac

echo "Hydra and SecLists installed successfully!"
