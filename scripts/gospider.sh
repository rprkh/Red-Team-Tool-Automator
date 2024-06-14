#!/bin/bash

# Update package list and install dependencies
sudo apt update

# Install GoSpider
sudo apt install -y gospider

# Verify installation
if command -v gospider &> /dev/null
then
    echo "GoSpider has been installed successfully."
else
    echo "Failed to install GoSpider."
fi
