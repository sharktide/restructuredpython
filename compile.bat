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

set /p arch="Was this run from an x64 tools prompt (y/n) >"
if "%arch%"=="y" (
    for %%F in (io.dll) do xcopy "%%F" "%SRC_DIR%/restructuredpython/lib/windows-libs/io64.dll" /Y
) else (
    for %%F in (io.dll) do xcopy "%%F" "%SRC_DIR%/restructuredpython/lib/windows-libs/io32.dll" /Y
)

echo Deleting copied files

del /Q C:\TempBuild

popd

echo Operation Completed

endlocal


@REM Copyright 2025 Rihaan Meher

@REM Licensed under the Apache License, Version 2.0 (the "License");
@REM you may not use this file except in compliance with the License.
@REM You may obtain a copy of the License at

@REM     http://www.apache.org/licenses/LICENSE-2.0

@REM Unless required by applicable law or agreed to in writing, software
@REM distributed under the License is distributed on an "AS IS" BASIS,
@REM WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@REM See the License for the specific language governing permissions and
@REM limitations under the License.