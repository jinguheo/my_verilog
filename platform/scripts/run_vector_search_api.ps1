. "$PSScriptRoot\_common.ps1"

Assert-CommandExists "go" "Install Go and add it to PATH before running vector-api."
$serviceRoot = Join-Path $PlatformRoot "services\vector-search-api"
Push-Location $serviceRoot
go mod tidy
go run ./cmd/vector-search-api
Pop-Location
