#!/bin/bash

# Clone httprobe repository
git clone https://github.com/tomnomnom/httprobe

# Navigate into httprobe directory
cd httprobe || exit

# Build main.go
go build main.go

# Rename main to httprobe
mv main httprobe

# Add httprobe to PATH
sudo mv httprobe /usr/local/bin/

cd ..

echo "httprobe has been successfully installed."