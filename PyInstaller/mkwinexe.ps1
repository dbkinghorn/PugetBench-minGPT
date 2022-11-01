#!/usr/bin/env bash

# PyInstaller build command for PugetBench-Numeric
# This one is simple enough that we don't need to use a spec file
#C:\Users\don\miniconda3\envs\dev-base\Scripts\pyinstaller --clean `
./venv/scripts/pyinstaller --clean `
    --console `
    --distpath='./dist' `
    --workpath='./build' `
    --onefile `
    ../pugetbench-mingpt.py

