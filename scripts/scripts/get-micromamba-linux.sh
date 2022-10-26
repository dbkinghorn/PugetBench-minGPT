#!/usr/bin/env bash

# Get the latest version of the micromamba-linux

# This will just grab the micromamba executable into the current directory
wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba --strip-components=1

