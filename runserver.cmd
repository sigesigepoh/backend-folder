@echo off
set SCRIPT_DIR=%~dp0
if exist "%SCRIPT_DIR%..\venv\Scripts\python.exe" (
  pushd "%SCRIPT_DIR%"
  "%SCRIPT_DIR%..\venv\Scripts\python.exe" manage.py runserver
  popd
) else (
  echo ERROR: Could not find %SCRIPT_DIR%..\venv\Scripts\python.exe
  echo Make sure the project root has the virtual environment folder named venv.
)
