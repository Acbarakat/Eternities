python -m pip install -r requirements.txt --upgrade
python -m pip install pypiwin32 kivy.deps.sdl2 kivy.deps.glew kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/ --upgrade
python -m pip install kivy --upgrade
garden install --update particlesystem
cd %USERPROFILE%\.kivy\garden\garden.particlesystem\setup.py install