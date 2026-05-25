param(
    [Parameter(Mandatory = $true)]
    [string]$KbDir,

    [Parameter(Mandatory = $true)]
    [int]$ExpectedCount,

    [Parameter(Mandatory = $true)]
    [string]$Label,

    [string]$OpenKbExe = "D:\MyWork\verilog\.venv-graphify\Scripts\openkb.exe",
    [string]$OllamaApiBase = "http://localhost:11434",
    [string]$OpenAiApiKey = "sk-dummy",
    [int]$SleepSeconds = 10,
    [int]$MaxStallRounds = 12
)

$ErrorActionPreference = "Continue"

function Get-HashCount {
    param([string]$HashesPath)

    if (-not (Test-Path $HashesPath)) {
        return 0
    }

    try {
        $json = Get-Content $HashesPath -Raw | ConvertFrom-Json
        return ($json.PSObject.Properties | Measure-Object).Count
    }
    catch {
        return 0
    }
}

$env:PYTHONIOENCODING = "utf-8"
$env:LITELLM_LOCAL_MODEL_COST_MAP = "True"
$env:OPENAI_API_KEY = $OpenAiApiKey
$env:OLLAMA_API_BASE = $OllamaApiBase

$hashesPath = Join-Path $KbDir ".openkb\hashes.json"
$logPath = Join-Path $KbDir ("resume_{0}.log" -f $Label)
$statusPath = Join-Path $KbDir ("resume_{0}.status.txt" -f $Label)

$stallRounds = 0
$round = 0

Set-Location $KbDir

"=== OpenKB resume loop started for $Label at $(Get-Date -Format o) ===" | Out-File -FilePath $logPath -Append -Encoding utf8

while ($true) {
    $current = Get-HashCount -HashesPath $hashesPath
    $status = "[$(Get-Date -Format o)] $Label current=$current expected=$ExpectedCount stall_rounds=$stallRounds round=$round"
    $status | Out-File -FilePath $statusPath -Encoding utf8
    $status | Out-File -FilePath $logPath -Append -Encoding utf8

    if ($current -ge $ExpectedCount) {
        "[$(Get-Date -Format o)] $Label complete." | Out-File -FilePath $logPath -Append -Encoding utf8
        break
    }

    $before = $current
    $round += 1

    "[$(Get-Date -Format o)] $Label starting add round $round" | Out-File -FilePath $logPath -Append -Encoding utf8
    & $OpenKbExe add ".\raw" *>&1 | Out-File -FilePath $logPath -Append -Encoding utf8
    $exitCode = $LASTEXITCODE

    $after = Get-HashCount -HashesPath $hashesPath
    "[$(Get-Date -Format o)] $Label finished add round $round exit_code=$exitCode before=$before after=$after" | Out-File -FilePath $logPath -Append -Encoding utf8

    if ($after -le $before) {
        $stallRounds += 1
    }
    else {
        $stallRounds = 0
    }

    if ($stallRounds -ge $MaxStallRounds) {
        "[$(Get-Date -Format o)] $Label stopped after $stallRounds consecutive stalled rounds." | Out-File -FilePath $logPath -Append -Encoding utf8
        break
    }

    Start-Sleep -Seconds $SleepSeconds
}

"=== OpenKB resume loop ended for $Label at $(Get-Date -Format o) ===" | Out-File -FilePath $logPath -Append -Encoding utf8
