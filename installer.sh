#!/bin/bash
sudo apt-get update -y
sudo apt install ffmpeg python3 -y
pip install -U pip setuptools wheel
pip install -r requirements.txt
