#!/bin/bash

echo "Checking if script is run as root"
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

echo "\nDetecting Linux distribution"

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

echo "\nChecking python and pip installation" 
if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null; then
    echo "python/pip installation not found" 
fi


echo "\nClone theHarvester repository"
git clone https://github.com/laramies/theHarvester.git

cd theHarvester

echo "\nInstall dependencies using pip"
pip install -r requirements.txt

python theHarvester.py --help

echo "\nTheHarvester help message displayed successfully."
