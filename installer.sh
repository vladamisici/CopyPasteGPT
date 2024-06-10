#!/bin/bash

pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

echo "Instalarea este completă. Rulați 'source venv/bin/activate' pentru a activa mediul virtual și apoi 'python copypasta.py' pentru a porni scriptul."
