. "$PSScriptRoot\_common.ps1"

$schema = Join-Path $SchemaRoot "postgres_schema.sql"
$extension = Join-Path $SchemaRoot "postgres_ontology_extension.sql"
Assert-PathExists $schema "Postgres schema"
Assert-PathExists $extension "Postgres ontology extension"

Get-Content -Raw $schema | docker exec -i verilog-postgres psql -U postgres -d verilog
if ($LASTEXITCODE -ne 0) {
  throw "Failed to load Postgres base schema."
}
Get-Content -Raw $extension | docker exec -i verilog-postgres psql -U postgres -d verilog
if ($LASTEXITCODE -ne 0) {
  throw "Failed to load Postgres ontology extension."
}
Write-Host "Postgres schemas loaded."
