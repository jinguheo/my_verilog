@echo off
cd /d %~dp0
where git >nul 2>nul
if errorlevel 1 (
  echo Git is not installed or not in PATH.
  exit /b 1
)
if exist .git (
  echo Git repository already initialized.
  exit /b 0
)
git init -b main
git add .
git commit -m "Initial commit: verilog skills workspace"
echo Done.
