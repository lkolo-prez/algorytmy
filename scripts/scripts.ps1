# PowerShell Skrypty Pomocnicze
# Użycie: . .\scripts.ps1 (źródłuj plik w sesji PowerShell)

function Validate-All {
    <#
    .SYNOPSIS
    Waliduje wszystkie pliki pseudokodu
    #>
    Write-Host "`n🔍 Walidacja wszystkich plików...`n" -ForegroundColor Cyan
    python validator.py --all
}

function Validate-List {
    <#
    .SYNOPSIS
    Waliduje wybraną listę
    .PARAMETER ListNumber
    Numer listy (1, 2, lub 3)
    #>
    param(
        [Parameter(Mandatory=$true)]
        [ValidateSet(1, 2, 3)]
        [int]$ListNumber
    )
    
    Write-Host "`n🔍 Walidacja listy $ListNumber...`n" -ForegroundColor Cyan
    python validator.py "lista_$ListNumber/*/zadanie.md"
}

function Validate-File {
    <#
    .SYNOPSIS
    Waliduje konkretny plik
    .PARAMETER Path
    Ścieżka do pliku zadanie.md
    #>
    param(
        [Parameter(Mandatory=$true)]
        [string]$Path
    )
    
    Write-Host "`n🔍 Walidacja pliku: $Path`n" -ForegroundColor Cyan
    python validator.py $Path
}

function New-Task {
    <#
    .SYNOPSIS
    Tworzy nowe zadanie (tryb interaktywny)
    #>
    Write-Host "`n📝 Generator nowego zadania`n" -ForegroundColor Green
    python new_task.py
}

function Show-Help {
    <#
    .SYNOPSIS
    Pokazuje dostępne komendy
    #>
    Write-Host "`n==========================================" -ForegroundColor Cyan
    Write-Host "  PSEUDOKOD - DOSTĘPNE KOMENDY (PowerShell)" -ForegroundColor White
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  Validate-All" -ForegroundColor Yellow -NoNewline
    Write-Host "           - Waliduj wszystkie pliki"
    Write-Host "  Validate-List " -ForegroundColor Yellow -NoNewline
    Write-Host "-ListNumber <1|2|3>" -ForegroundColor Green -NoNewline
    Write-Host " - Waliduj listę"
    Write-Host "  Validate-File " -ForegroundColor Yellow -NoNewline
    Write-Host "-Path <ścieżka>" -ForegroundColor Green -NoNewline
    Write-Host "      - Waliduj plik"
    Write-Host "  New-Task" -ForegroundColor Yellow -NoNewline
    Write-Host "                - Utwórz nowe zadanie"
    Write-Host "  Show-Help" -ForegroundColor Yellow -NoNewline
    Write-Host "               - Pokaż tę pomoc"
    Write-Host ""
    Write-Host "Przykłady:" -ForegroundColor Cyan
    Write-Host "  Validate-All" -ForegroundColor Green
    Write-Host "  Validate-List -ListNumber 1" -ForegroundColor Green
    Write-Host "  Validate-File -Path lista_1/1_suma_elementow/zadanie.md" -ForegroundColor Green
    Write-Host "  New-Task" -ForegroundColor Green
    Write-Host ""
    Write-Host "Aliasy:" -ForegroundColor Cyan
    Write-Host "  val     = Validate-All" -ForegroundColor Gray
    Write-Host "  val1    = Validate-List -ListNumber 1" -ForegroundColor Gray
    Write-Host "  val2    = Validate-List -ListNumber 2" -ForegroundColor Gray
    Write-Host "  val3    = Validate-List -ListNumber 3" -ForegroundColor Gray
    Write-Host "  newtask = New-Task" -ForegroundColor Gray
    Write-Host ""
}

# Aliasy
Set-Alias -Name val -Value Validate-All
Set-Alias -Name val1 -Value { Validate-List -ListNumber 1 }
Set-Alias -Name val2 -Value { Validate-List -ListNumber 2 }
Set-Alias -Name val3 -Value { Validate-List -ListNumber 3 }
Set-Alias -Name newtask -Value New-Task
Set-Alias -Name help-pseudo -Value Show-Help

# Automatycznie pokaż pomoc przy źródłowaniu
Write-Host "`n✅ Skrypty załadowane!" -ForegroundColor Green
Show-Help

Export-ModuleMember -Function * -Alias *
