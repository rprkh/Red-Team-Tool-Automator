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

echo "Checking python and pip installation" 
if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null; then
    echo "python/pip installation Not Found" 
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

# Function to install a package using the appropriate package manager
install_package() {
    local package=$1

    case $OS in
        ubuntu|debian|kali)
            apt-get install -y "$package" || { echo "Failed to install $package. Please try again."; exit 1; }
            ;;
        centos|rhel|fedora)
            yum install -y "$package" || { echo "Failed to install $package. Please try again."; exit 1; }
            ;;
        arch)
            pacman -Sy --noconfirm "$package" || { echo "Failed to install $package. Please try again."; exit 1; }
            ;;
        *)
            echo "Unsupported Linux distribution: $OS"
            exit 1
            ;;
    esac
}

# Update package lists and install necessary packages
case $OS in
    ubuntu|debian|kali)
        install_package "dnsenum"
        ;;
    centos|rhel|fedora)
        install_package "dnsenum"
        ;;
    arch)
        install_package "dnsenum"
        ;;
    *)
        echo "Unsupported Linux distribution: $OS"
        exit 1
        ;;
esac

echo "dnsenum Installed Successfully"