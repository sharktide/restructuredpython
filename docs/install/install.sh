#!/bin/bash

echo "Installing..."
pip install --upgrade restructuredpython

read -p "Install Visual Studio Code extension? (y/n): " input
if [[ "$input" == "y" || "$input" == "Y" ]]; then
    echo "Installing extension..."
    code --install-extension RihaanMeher.restructuredpython --force
fi
