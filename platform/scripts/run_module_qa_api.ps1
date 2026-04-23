. "$PSScriptRoot\_common.ps1"

Assert-CommandExists "go" "Install Go and add it to PATH before running module-api."
$serviceRoot = Join-Path $PlatformRoot "services\module-qa-api"
Push-Location $serviceRoot
go mod tidy
go run ./cmd/module-qa-api
Pop-Location
