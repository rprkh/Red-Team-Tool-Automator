#!/bin/bash

# Check if the script is being run with sudo
if [[ $EUID -ne 0 ]]; then
  echo "Please run this script with sudo."
  exit 1
fi

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git and try again."
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

echo "Install dependencies and recon-ng based on the distribution"
case $OS in
    ubuntu|debian|kali)
        apt-get install -y python3-pip || { echo "Failed to install Python3-pip. Please try again."; exit 1; }
        ;;
    centos|rhel|fedora)
        yum install -y python3-pip || { echo "Failed to install Python3-pip. Please try again."; exit 1; }
        ;;
    arch)
        pacman -Sy --noconfirm python-pip || { echo "Failed to install Python-pip. Please try again."; exit 1; }
        ;;
    *)
        echo "Unsupported Linux distribution: $OS"
        exit 1
        ;;
esac

# Clone the repository
git clone https://github.com/lanmaster53/recon-ng.git || { echo "Failed to clone repository."; exit 1; }
cd recon-ng

# Install recon-ng dependencies
pip3 install -r REQUIREMENTS || { echo "Failed to install recon-ng dependencies. Please try again."; exit 1; }

echo "recon-ng installed successfully!"