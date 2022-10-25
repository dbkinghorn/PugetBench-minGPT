## Notes for building exe with PyInstaller

This dir [PugetBench-Numeric/PyInstaller] contains a venv dir which should contain a minimal python + pyinstaller to use as a build environment.
mm-bin contains micromamba which can be use to create the environment

```
mm-bin/micromamba create -p ./venv -r ./mm-bin pyinstaller -c conda-forge
```

The shell script mkexe.sh will put the build files and dist dir in this dir.

```
#!/usr/bin/env bash

# PyInstaller build command for PugetBench-mingpt
# This one is simple enough that we don't need to use a spec file
./venv/bin/pyinstaller --clean \
    --distpath='./dist' \
    --workpath='./build' \
    --onefile \
    ../pugetbench-mingpt.py

```

Then just bundle as tar.gz or zip including the new exe
pugetbench-minpgt -- the setup runner program (see --help)
mm/micromamba -- the micromamba conda package to do the pytorch setup
chargpt.py -- the benchmark (training character based Shakespeare generator )
input.txt -- the Shakespeare training data
mingpt -- Karpathy's minGPT python code
