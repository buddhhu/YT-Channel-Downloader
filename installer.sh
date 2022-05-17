#!/bin/bash
sudo apt-get update -y
sudo apt install ffmpeg -y
pip install -q -U pip setuptools wheel
pip install -q -r requirements.txt
