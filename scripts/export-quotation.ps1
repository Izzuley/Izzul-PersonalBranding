param(
    [Parameter(Mandatory=$true)][string]$Html,
    [Parameter(Mandatory=$true)][string]$Pdf,
    [string]$Browser
)
$ErrorActionPreference = 'Stop'
$source = (Resolve-Path -LiteralPath $Html).Path
if ([IO.Path]::GetExtension($source) -ne '.html') { throw 'Input must be an HTML file.' }
$destination = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Pdf)
if ([IO.Path]::GetExtension($destination) -ne '.pdf') { throw 'Output must have a .pdf extension.' }
if (Test-Path -LiteralPath $destination) { throw 'Output exists. Choose a new filename or remove it deliberately first.' }
if (-not $Browser) {
    $Browser = @(
        "${env:ProgramFiles}\Google\Chrome\Application\chrome.exe",
        "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
        "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
    ) | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
}
if (-not $Browser -or -not (Test-Path -LiteralPath $Browser)) { throw 'Chrome or Edge not found. Pass -Browser with its executable path, or use Ctrl+P.' }
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) | Out-Null
# An isolated profile avoids interacting with open browser sessions.
$profile = Join-Path ([IO.Path]::GetTempPath()) ('quotation-browser-' + [guid]::NewGuid())
$uri = ([System.Uri]$source).AbsoluteUri
$arguments = @('--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
    '--no-pdf-header-footer', '--timeout=10000', ('--user-data-dir="' + $profile + '"'),
    ('--print-to-pdf="' + $destination + '"'), ('"' + $uri + '"'))
$process = Start-Process -FilePath $Browser -ArgumentList $arguments -WindowStyle Hidden -PassThru
if (-not $process.WaitForExit(60000)) { $process.Kill(); throw 'PDF export timed out. Try the browser print dialog.' }
if (-not (Test-Path -LiteralPath $destination) -or (Get-Item -LiteralPath $destination).Length -eq 0) {
    throw 'Browser did not create a PDF. Inspect the HTML in Chrome or Edge and use Ctrl+P.'
}
Write-Output "Created $destination"
Write-Output "Inspect every PDF page before sending. Temporary browser profile: $profile"
