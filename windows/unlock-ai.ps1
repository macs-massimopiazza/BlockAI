# ============================================

# Script SBLOCCO domini AI su Windows

# Eseguire come AMMINISTRATORE

# ============================================

$hostsPath = "$env:SystemRoot\System32\drivers\etc\hosts"
$backupPath = "$hostsPath.backup-unblock-$(Get-Date -Format 'yyyyMMdd-HHmmss')"

Write-Host "Backup hosts file..."
Copy-Item $hostsPath $backupPath -Force

# Legge tutto il file

$content = Get-Content $hostsPath

$newContent = @()
$skip = $false
$removed = 0

foreach ($line in $content) {

```
if ($line -eq "# BLOCCO AI - AUTO") {
    $skip = $true
    $removed++
    continue
}

if ($skip -and $line -match "^0\.0\.0\.0\s+") {
    $removed++
    continue
}

$skip = $false
$newContent += $line
```

}

# Scrive il file pulito

Set-Content -Path $hostsPath -Value $newContent -Force

Write-Host ""
Write-Host "Flush DNS cache..."

ipconfig /flushdns | Out-Null

Write-Host ""
Write-Host "Operazione completata!"
Write-Host "Righe rimosse: $removed"
Write-Host "Backup salvato in: $backupPath"
