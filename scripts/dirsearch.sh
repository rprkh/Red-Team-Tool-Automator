#!/bin/bash

# Check if script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
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

# Install Python3 and pip3 if they are not installed
install_python_and_pip() {
    case $OS in
        ubuntu|debian|kali)
            apt-get update || { echo "Failed to update apt cache. Please check your internet connection or try again later."; exit 1; }
            apt-get install -y python3 python3-pip || { echo "Failed to install Python3 and pip3. Please try again."; exit 1; }
            ;;
        centos|rhel|fedora)
            yum install -y python3 python3-pip || { echo "Failed to install Python3 and pip3. Please try again."; exit 1; }
            ;;
        arch)
            pacman -Sy --noconfirm python python-pip || { echo "Failed to install Python and pip. Please try again."; exit 1; }
            ;;
        *)
            echo "Unsupported Linux distribution: $OS"
            exit 1
            ;;
    esac
}

if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null; then
    echo "Python3 and/or pip3 not found. Installing..."
    install_python_and_pip
fi

# Install dirsearch globally
install_dirsearch() {
    case $OS in
        ubuntu|debian|kali)
            apt-get install -y dirsearch || { echo "Failed to install dirsearch using apt. Trying pip..."; pip3 install dirsearch || { echo "Failed to install dirsearch using pip. Please try manually."; exit 1; } }
            ;;
        centos|rhel|fedora|arch)
            pip3 install dirsearch || { echo "Failed to install dirsearch using pip. Please try manually."; exit 1; }
            ;;
        *)
            echo "Unsupported Linux distribution: $OS"
            exit 1
            ;;
    esac
}

echo "Installing dirsearch..."
install_dirsearch

echo "dirsearch installed successfully!"
