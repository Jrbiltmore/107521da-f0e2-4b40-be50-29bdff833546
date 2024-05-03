#!/bin/bash

# Ensure script is run as root
if [ "$(id -u)" != "0" ]; then
    echo "Error: This script must be run as root."
    exit 1
fi

# Update package repositories and install essential packages
echo "Updating package repositories and installing essential packages..."
apt-get update
apt-get install -y python3 python3-pip git wget curl unzip

# Install additional dependencies
echo "Installing additional dependencies..."
pip3 install numpy pandas matplotlib

# Install required system packages
echo "Installing required system packages..."
apt-get install -y build-essential libssl-dev libffi-dev

# Install quantum computing libraries (e.g., Qiskit)
echo "Installing quantum computing libraries..."
pip3 install qiskit

# Set up virtual environment for Python projects (optional)
echo "Setting up virtual environment for Python projects..."
pip3 install virtualenv
virtualenv venv
source venv/bin/activate

# Clone project repository
echo "Cloning project repository..."
git clone https://github.com/yourusername/yourproject.git
cd yourproject

# Download additional data or resources if needed
echo "Downloading additional data or resources..."
wget -O data.zip https://example.com/data.zip
unzip data.zip -d data

echo "Environment setup completed."
