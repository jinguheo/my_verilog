. "$PSScriptRoot\_common.ps1"

$envPath = Ensure-PlatformEnv
Push-Location $RuntimeRoot
docker compose --env-file $envPath up -d
if ($LASTEXITCODE -ne 0) {
  throw "Docker Compose failed."
}
Pop-Location
Write-Host "Stack started."
