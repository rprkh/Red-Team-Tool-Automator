#!/bin/bash

echo "Checking if script is run as root"
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
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

echo "Checking python and pip installation" 
if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null; then
    echo "python/pip installation Not Found" 
    exit 1
fi

echo "Clone the Metagoofil repository"
git clone https://github.com/opsdisk/metagoofil

cd metagoofil

echo "\nInstall dependencies using pip"
pip install -r requirements.txt

metagoofil --help

echo "\nMetagoofil installation and help message displayed successfully!"
