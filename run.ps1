param(
  [switch]$NoBrowser
)

$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

Write-Host '🚀 Starting PipeDL backend...' -ForegroundColor Cyan

$guiPath = Join-Path $PSScriptRoot 'yt-dlp-gui'
if (-not (Test-Path $guiPath)) {
  throw "yt-dlp-gui folder not found at: $guiPath"
}

Set-Location $guiPath

if (-not $NoBrowser) {
  Start-Process 'http://localhost:5000' | Out-Null
}

python app.py
