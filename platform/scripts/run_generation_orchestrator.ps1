. "$PSScriptRoot\_common.ps1"

Assert-CommandExists "go" "Install Go and add it to PATH before running generator."
$serviceRoot = Join-Path $PlatformRoot "services\generation-orchestrator"
Push-Location $serviceRoot
go mod tidy
go run ./cmd/generation-orchestrator
Pop-Location
