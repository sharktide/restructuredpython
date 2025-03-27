@echo off
echo Installing...
pip install --upgrade restructuredpython
set /p input= Install Visual Studio Code extension? (y/n)
IF %input%==y (
    echo Sup
    code --install-extension RihaanMeher.restructuredpython --force
)
IF %input%==Y (
    code --install-extension RihaanMeher.restructuredpython --force
)
PAUSE