. "$PSScriptRoot\_common.ps1"

New-Item -ItemType Directory -Force -Path (Join-Path $RuntimeRoot "volumes\postgres") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $RuntimeRoot "volumes\neo4j\data") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $RuntimeRoot "volumes\neo4j\logs") | Out-Null
Ensure-OutRoot
Write-Host "Folders initialized."
