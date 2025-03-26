#!/bin/bash
# Install system dependencies
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt update && sudo apt install -y portaudio19-dev
elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install portaudio
fi

# Install Python dependencies
pip install -r requirements.txt
