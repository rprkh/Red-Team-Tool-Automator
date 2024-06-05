#!/bin/bash

# Function to check if running on Windows
is_windows() {
    case "$(uname -s)" in
        CYGWIN*|MINGW32*|MSYS*|MINGW*)
            return 0
            ;;
        *)
            return 1
            ;;
    esac
}

# Check if the script is being run with sudo (only if not on Windows)
if ! is_windows && [[ $EUID -ne 0 ]]; then
    echo "Please run this script with sudo."
    exit 1
fi

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git and try again."
    exit 1
fi

# Function to install dependencies on Linux
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

# Install dependencies based on the detected OS
if is_windows; then
    echo "Running on Windows..."
else
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

    case $OS in
        ubuntu|debian|kali)
            # apt-get update || { echo "Failed to update apt cache. Please check your internet connection or try again later."; exit 1; }
            install_package "python3-pip"
            ;;
        centos|rhel|fedora)
            install_package "python3-pip"
            ;;
        arch)
            install_package "python-pip"
            ;;
        *)
            echo "Unsupported Linux distribution: $OS"
            exit 1
            ;;
    esac
fi

# Check if wfuzz is already installed
if [ -d "wfuzz" ]; then
    echo "wfuzz has already been successfully installed on your system."
else
    pip install wfuzz

    if [ $? -ne 0 ]; then
        echo "Error: Failed to install wfuzz using pip."
        exit 1
    fi

    git clone https://github.com/xmendez/wfuzz.git

    if [ $? -ne 0 ]; then
        echo "Error: Failed to clone the repository."
        exit 1
    fi

    cd wfuzz

    wfuzz -z help

    echo "wfuzz installation and setup successfully completed"

    cd ..
fi
