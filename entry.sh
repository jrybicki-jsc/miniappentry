#!/bin/sh
echo "Bla blah"
python -m pip install docker pyyaml
python /app/builder_service.py
