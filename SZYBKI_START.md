# Szybki Start

## Najważniejsze Narzędzia

### 1. **validator.py** (NAJWAŻNIEJSZE!)
Sprawdza poprawność składni pseudokodu.

```bash
# Pojedynczy plik
python validator.py workspace/lista_1/1_suma_elementow/zadanie.md

# Wszystkie zadania z listy 1
python validator.py workspace/lista_1/*/zadanie.md

# Cała lista 2
python validator.py workspace/lista_2/*/zadanie.md
```

### 2. **interpreter.py** 
Uruchamia algorytmy w pseudokodzie.

```bash
# Podstawowe uruchomienie
python interpreter.py workspace/lista_1/1_suma_elementow/zadanie.md --input=5,1,2,3,4,5

# Tryb debug (krok po kroku)
python interpreter.py workspace/lista_1/1_suma_elementow/zadanie.md --input=5,1,2,3,4,5 --debug
```

## Materiały do Nauki

### workspace/ - 32 zadania
- **lista_1/** - 9 zadań podstawowych
- **lista_2/** - 11 zadań zaawansowanych 
- **lista_3/** - 12 zadań rekurencyjnych

Każde zadanie ma:
- `zadanie.md` - kod algorytmu
- `opis.md` - opis i wyjaśnienie

### examples/ - Przykłady
- suma.md - Suma elementów tablicy
- min_max.md - Znajdowanie min i max
- sortowanie_babelkowe.md - Sortowanie bąbelkowe
- wyszukiwanie_binarne.md - Wyszukiwanie binarne
- silnia.md - Silnia (rekurencyjnie)

## Dodatkowe Narzędzia

W katalogu **scripts/**:
- `test_runner.py` - Uruchamianie testów
- `new_task.py` - Generator nowych zadań
- `scripts.ps1` - Skrypty PowerShell
- `Makefile` - Automatyzacja

## Dokumentacja

W katalogu **docs/**:
- README_PL.md - Pełna dokumentacja po polsku
- README_EN.md - Full English documentation
- SCIAGAWKA.html - Ściągawka do wydruku
- PRZEWODNIK_SRODOWISKA.md - Szczegółowy przewodnik
- Lista 1/2/3.pdf - Materiały z kursu

## Typowy Workflow

```bash
# 1. Przeczytaj opis zadania
cat workspace/lista_1/1_suma_elementow/opis.md

# 2. Zobacz kod
cat workspace/lista_1/1_suma_elementow/zadanie.md

# 3. ZWALIDUJ (najważniejsze!)
python validator.py workspace/lista_1/1_suma_elementow/zadanie.md

# 4. Uruchom z debugiem
python interpreter.py workspace/lista_1/1_suma_elementow/zadanie.md --input=5,1,2,3,4,5 --debug
```

## Struktura Katalogów

```
algorytmy/
validator.py # Walidator (najważniejszy!)
interpreter.py # Interpreter
README.md # Główna dokumentacja
requirements.txt # Zależności
LICENSE # Licencja MIT

workspace/ # 32 zadania do nauki
lista_1/ # 9 zadań
lista_2/ # 11 zadań
lista_3/ # 12 zadań

examples/ # Przykłady
tests/ # Testy
scripts/ # Narzędzia pomocnicze
docs/ # Dokumentacja
.vscode/ # Konfiguracja VS Code
```

## Wskazówki

- **Zawsze waliduj przed uruchomieniem!** (`validator.py`)
- Używaj trybu `--debug` aby zobaczyć wykonanie krok po kroku
- Zacznij od `examples/` jeśli jesteś początkujący
- Pracuj systematycznie: lista_1 → lista_2 → lista_3
- Czytaj `opis.md` przed analizą kodu

## Pomoc

- Pełna dokumentacja: `docs/README_PL.md`
- Ściągawka: `docs/SCIAGAWKA.html` (otwórz w przeglądarce)
- Przewodnik: `docs/PRZEWODNIK_SRODOWISKA.md`
- Workspace: `workspace/WORKSPACE_GUIDE.md`

---

**Powodzenia w nauce algorytmów! **
