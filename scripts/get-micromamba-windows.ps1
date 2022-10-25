
# This will get the latest version of micromamba
# requires 7zip be installed on Windows system

Invoke-Webrequest -URI https://micromamba.snakepit.net/api/micromamba/win-64/latest -OutFile micromamba.tar.bz2
C:\PROGRA~1\7-Zip\7z.exe x micromamba.tar.bz2 -aoa
C:\PROGRA~1\7-Zip\7z.exe x micromamba.tar -ttar -aoa -r Library\bin\micromamba.exe

