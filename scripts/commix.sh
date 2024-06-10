#!/bin/bash

# Update the package list
echo "Updating package list..."
sudo apt update

# Install Commix
echo "Installing Commix..."
sudo apt install -y commix

# Verify installation
echo "Verifying Commix installation..."
commix --version

echo "Commix installation complete."
