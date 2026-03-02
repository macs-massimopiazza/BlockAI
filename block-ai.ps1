# ============================================

# Script blocco domini AI su Windows

# Eseguire come AMMINISTRATORE

# ============================================

$hostsPath = "$env:SystemRoot\System32\drivers\etc\hosts"
$backupPath = "$hostsPath.backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"

# Domini da bloccare

$domains = @(
"chat.openai.com",
"openai.com",
"api.openai.com",
"platform.openai.com",
"gemini.google.com",
"bard.google.com",
"generativelanguage.googleapis.com",
"copilot.microsoft.com",
"bing.com",
"edgeservices.bing.com",
"claude.ai",
"api.anthropic.com",
"perplexity.ai",
"midjourney.com",
"stability.ai",
"api.stability.ai",
"poe.com",
"huggingface.co",
"api-inference.huggingface.co",
"x.ai",
"grok.x.ai"
)

Write-Host "Backup hosts file..."
Copy-Item $hostsPath $backupPath -Force

# Legge contenuto esistente

$content = Get-Content $hostsPath -ErrorAction SilentlyContinue

# Marker

$marker = "# BLOCCO AI - AUTO"

if ($content -notcontains $marker) {
Add-Content $hostsPath "`n$marker"
}

$added = 0

foreach ($domain in $domains) {
$entry = "0.0.0.0 $domain"

```
if ($content -notcontains $entry) {
    Add-Content $hostsPath $entry
    Write-Host "Bloccato: $domain"
    $added++
}
```

}

Write-Host ""
Write-Host "Flush DNS cache..."

ipconfig /flushdns | Out-Null

Write-Host ""
Write-Host "Operazione completata!"
Write-Host "Domini aggiunti: $added"
Write-Host "Backup salvato in: $backupPath"
