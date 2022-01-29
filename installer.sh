#!/bin/bash
apt-update -y
apt install ffmpeg python3 -y
pip install -U pip setuptools wheel
pip install -r requirements.txt
