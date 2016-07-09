#!/bin/sh
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
pyenv shell 3.5.1
python Run.py
