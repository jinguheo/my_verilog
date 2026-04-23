Set-Location $PSScriptRoot
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git is not installed or not in PATH."
    exit 1
}
if (Test-Path .git) {
    Write-Host "Git repository already initialized."
    exit 0
}
git init -b main
git add .
git commit -m "Initial commit: verilog skills workspace"
Write-Host "Done."
