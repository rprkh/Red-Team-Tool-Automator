#!/bin/bash

# Function to install feroxbuster on apt-based systems
install_on_apt() {
    echo "Installing feroxbuster on a system using apt..."
    curl -sLO https://github.com/epi052/feroxbuster/releases/latest/download/feroxbuster_amd64.deb.zip
    unzip feroxbuster_amd64.deb.zip
    sudo apt install ./feroxbuster_*_amd64.deb
    echo "Feroxbuster installation complete on apt-based system."
    
    echo "Installing seclists on a system using apt..."
    sudo apt update
    sudo apt install seclists -y
    echo "Seclists installation complete on apt-based system."
}

# Function to install feroxbuster on macOS
install_on_mac() {
    echo "Installing feroxbuster on macOS..."
    brew install feroxbuster
    echo "Feroxbuster installation complete on macOS."
    
    echo "Installing seclists on macOS..."
    brew install seclists
    echo "Seclists installation complete on macOS."
}

# Function to display PowerShell commands for Windows installation
install_on_windows() {
    echo "To install Feroxbuster on Windows, execute the following PowerShell commands:"
    echo "Invoke-WebRequest https://github.com/epi052/feroxbuster/releases/latest/download/x86_64-windows-feroxbuster.exe.zip -OutFile feroxbuster.zip"
    echo "Expand-Archive .\\feroxbuster.zip"
    echo ".\\feroxbuster\\feroxbuster.exe -V"
    
    echo "To install Seclists on Windows, execute the following PowerShell commands:"
    echo "Invoke-WebRequest https://github.com/danielmiessler/SecLists/archive/refs/heads/master.zip -OutFile seclists.zip"
    echo "Expand-Archive .\\seclists.zip"
    echo "Move-Item .\\SecLists-master .\\seclists"
}

# Detect the OS and install accordingly
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if command -v apt > /dev/null; then
        install_on_apt
    else
        echo "This script currently supports apt-based systems on Linux."
        exit 1
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    if command -v brew > /dev/null; then
        install_on_mac
    else
        echo "Homebrew not found. Please install Homebrew and try again."
        exit 1
    fi
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    install_on_windows
else
    echo "Unsupported OS type: $OSTYPE"
    exit 1
fi
