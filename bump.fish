#!/bin/fish
rm -rf dist
rm -rf *.egg-info

python bump.py
python setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ --password $TWINE_PW dist/*
