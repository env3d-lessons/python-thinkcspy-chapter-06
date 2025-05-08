#!/bin/bash

sudo apt-get update
sudo apt-get install -y xvfb
pip install pyvirtualdisplay Pillow imageio pytest
# Prevent extensions from being installed with 0555 permissions
chmod 555 ~/.vscode-remote/extensions/
