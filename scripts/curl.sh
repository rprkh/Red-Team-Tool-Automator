#!/bin/bash

# Define variables
REPO_URL="https://github.com/curl/curl.git"
INSTALL_DIR="/usr/local/curl"

# Check if git is installed
if ! command -v git &> /dev/null
then
    echo "git could not be found. Please install git and try again."
    exit 1
fi

# Check if build-essential is installed (for make and gcc)
if ! dpkg -s build-essential &> /dev/null
then
    echo "build-essential is not installed. Installing it now..."
    sudo apt-get install -y build-essential
fi

# Clone the Curl repository
echo "Cloning the Curl repository..."
git clone $REPO_URL $INSTALL_DIR

# Change to the repository directory
cd $INSTALL_DIR

# Build Curl
echo "Building Curl..."
./buildconf
./configure
make

# Add to PATH
echo "Adding Curl to PATH..."
export PATH=$PATH:$INSTALL_DIR/src
echo "export PATH=\$PATH:$INSTALL_DIR/src" >> ~/.bashrc
source ~/.bashrc

# Verify installation
echo "Verifying Curl installation..."
curl --version

echo "Curl installation completed successfully."
