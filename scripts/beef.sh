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

BEEF_DIR="/usr/local/beef"

if [ ! -d "$BEEF_DIR" ]; then
    read -p "BeEF directory '$BEEF_DIR' does not exist. Create it? (y/N) " -r
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
      echo "Exiting..."
      exit 1
    fi
    mkdir -p "$BEEF_DIR"
  fi

echo "Sucessfully Created BeEf Directory"

git clone https://github.com/beefproject/beef.git "$BEEF_DIR"

echo "Sucessfully Cloned BeEf"

cd "$BEEF_DIR"

echo "Starting Dependencies Installation" 

if [[ "$OS" == "ubuntu" || "$OS" == "debian" || "$OS" == "kali" ]]; then
  apt-get install -y ruby-dev libpq-dev build-essential autoconf bison libssl-dev libreadline6-dev zlib1g-dev libcurl4-openssl-dev libjansson-dev libffi-dev libxml2-dev libxslt1-dev rake

elif [[ "$OS" == "arch" ]]; then
  pacman -Sy
  pacman -S ruby ruby-dev postgresql-devel autoconf bison openssl readline zlib curl jansson libffi libxml2 libxslt rake

elif [[ "$OS" == "rhel" || "$OS" == "centos" || "$OS" == "fedora" ]]; then
  dnf update -y
  dnf install -y ruby ruby-devel postgresql-devel autoconf bison openssl readline zlib curl jansson libffi libxml2 libxslt ruby-gem-rake

else
  echo "Unsupported Linux distribution: $OS"
fi

echo "Dependencies Installed Successfully" 

gem install bundler --no-document

echo "Starting Bundle Installation"

bundle install

echo "Bundle Installation Completed Successfully"

./beef 