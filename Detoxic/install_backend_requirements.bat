@echo off
REM Run this from Windows Command Prompt (cmd.exe). It activates the venv and installs backend requirements.
cd /d "%~dp0"
if not exist ".venv\Scripts\activate.bat" (
  echo Virtual environment not found at .venv\Scripts\activate.bat
  echo Create the venv first or adjust this script.
  pause
  exit /b 1
)
call ".venv\Scripts\activate.bat"
echo Installing backend Python requirements...
python -m pip install -r Backend\App\requirements.txt
echo Backend requirements installation finished.
pause
