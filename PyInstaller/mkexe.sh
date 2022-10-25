#!/usr/bin/env bash

# PyInstaller build command for PugetBench-mingpt
# This one is simple enough that we don't need to use a spec file
./venv/bin/pyinstaller --clean \
    --distpath='./dist' \
    --workpath='./build' \
    --onefile \
    ../pugetbench-mingpt.py
