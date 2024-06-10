#!/bin/bash

# Clone the repository
echo "Cloning the repository..."
git clone https://github.com/jaeles-project/gospider.git

# Check if cloning was successful
if [ $? -ne 0 ]; then
    echo "Failed to clone the repository."
    exit 1
fi

# Navigate into the repository directory
cd gospider

# Build the Docker container
echo "Building the Docker container..."
docker build -t gospider:latest .

# Check if Docker build was successful
if [ $? -ne 0 ]; then
    echo "Failed to build the Docker container."
    exit 1
fi

# Run the Docker container
echo "Running the Docker container..."
docker run -t gospider -h

# Check if Docker run was successful
if [ $? -ne 0 ]; then
    echo "Failed to run the Docker container."
    exit 1
fi

echo "Done!"
