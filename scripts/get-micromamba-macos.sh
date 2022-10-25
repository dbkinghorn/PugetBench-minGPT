#!/usr/bin/env bash

# Get the latest version of the micromamba-macos

curl -Ls https://micromamba.snakepit.net/api/micromamba/osx-64/latest | tar -xvj bin/micromamba
mv bin/micromamba ./micromamba
chmod +x micromamba

