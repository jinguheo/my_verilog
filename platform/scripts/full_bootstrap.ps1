. "$PSScriptRoot\_common.ps1"

& "$PSScriptRoot\init_folders.ps1"
Ensure-PlatformEnv | Out-Null
& "$PSScriptRoot\start_stack.ps1"
Start-Sleep -Seconds 8
& "$PSScriptRoot\load_postgres_schema.ps1"
& "$PSScriptRoot\generate_seed_and_labels.ps1"
& "$PSScriptRoot\load_neo4j.ps1"
Write-Host "Bootstrap complete for OpenTitan + Ibex."
