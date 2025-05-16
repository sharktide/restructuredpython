@echo off
setlocal enabledelayedexpansion
echo This compiles the C libraries in a external enviornment using MSVC, then copies them to the appropriate locations in this repo.
echo Requirements: xcopy.exe on PATH
echo Requirements: MSVC cl.exe
echo Requirements: This must be run from either the Developer PWSH/CMD for VS or the x64 Native Tools Prompt

set SRC_DIR=%CD%
set DEST=C:\TempBuild

if not exist "%DEST%" mkdir "%DEST%"

xcopy "%SRC_DIR%\*" "%DEST%" /E /H /C /I /exclude:exclude.txt

pushd "C:\TempBuild"
cl /LD restructuredpython/include/io.c

for %%F in (*.dll) do xcopy "%%F" "%SRC_DIR%/restructuredpython/lib" /Y

echo Deleting copied files

del /Q "%DEST%\*.*"

popd

echo Operation Completed

endlocal
