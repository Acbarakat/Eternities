#! /bin/sh

sudo add-apt-repository ppa:kivy-team/kivy -y
sudo add-apt-repository ppa:mc3man/trusty-media -y

sudo apt-get update

sudo apt-get install -y python-pip build-essential  git python python-dev ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev

sudo apt-get install -y python-kivy

python -m pip install -r requirements.txt -- upgrade