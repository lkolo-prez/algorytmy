# VS Code - Konfiguracja Środowiska Pseudokodu

Ten folder zawiera pełną konfigurację środowiska do pisania pseudokodu w VS Code.

---

## 📁 Zawartość

| Plik | Opis |
|------|------|
| `pseudocode.tmLanguage.json` | Gramatyka TextMate - podświetlanie składni |
| `pseudocode.code-snippets` | 16 snippetów do szybkiego pisania |
| `language-configuration.json` | Auto-zamykanie nawiasów, wcięcia |
| `tasks.json` | 5 tasków do walidacji pseudokodu |
| `settings.json` | Ustawienia projektu |
| `keybindings.json` | Skróty klawiszowe |

---

## 🚀 Automatyczna Aktywacja

Wszystkie pliki są **automatycznie rozpoznawane** przez VS Code gdy:
1. Otworzysz folder jako workspace
2. Otworzysz plik `.md` w projekcie

**Nie wymaga instalacji rozszerzeń!**

---

## ⌨️ Skróty Klawiszowe

| Skrót | Akcja |
|-------|-------|
| `Ctrl+Shift+B` | Waliduj bieżący plik (domyślny task) |
| `Ctrl+Shift+V` | Waliduj bieżący plik (alternatywny) |
| `Ctrl+Alt+V` | Waliduj wszystkie pliki |
| `Ctrl+Alt+1` | Waliduj listę 1 |
| `Ctrl+Alt+2` | Waliduj listę 2 |
| `Ctrl+Alt+3` | Waliduj listę 3 |

---

## 🎨 Snippety Dostępne

Wpisz skrót + Tab w bloku ` ```pseudocode `:

### Podstawowe
- `alg` - Szablon algorytmu
- `if` - If statement
- `ife` - If-else statement
- `for` - For loop
- `fors` - For loop z krokiem
- `while` - While loop

### Operacje
- `let` - Przypisanie
- `read` - Wczytanie
- `write` - Wypisanie
- `arr` - Tablica 1D
- `arr2d` - Tablica 2D

### Gotowe Algorytmy
- `readarr` - Wczytaj tablicę
- `sumarr` - Suma tablicy
- `findmin` - Znajdź minimum
- `findmax` - Znajdź maksimum
- `swap` - Zamień zmienne

---

## 🔧 Ustawienia

### Auto-zamykanie
- `{` automatycznie dodaje `}`
- `[` automatycznie dodaje `]`
- `(` automatycznie dodaje `)`
- `"` automatycznie dodaje `"`

### Auto-formatowanie
- Tab size: 2 spacje
- Automatyczne wcięcie po `{`
- Składanie bloków kodu (folding)

### Sugestie
- Włączone dla wszystkich plików .md
- Snippety mają priorytet
- Quick suggestions aktywne

---

## 📝 Jak Używać

### 1. Otwórz Projekt
```bash
code .
```

### 2. Edytuj Plik
```
lista_X/Y_nazwa/zadanie.md
```

### 3. W Bloku Pseudocode
````markdown
```pseudocode
alg[Tab]  ← Wstaw szablon
for[Tab]  ← Wstaw pętlę
if[Tab]   ← Wstaw warunek
```
````

### 4. Waliduj
```
Ctrl+Shift+B
```

---

## 🎯 Podświetlanie Składni

### Kolorowane Elementy

- **Słowa kluczowe:** algorithm, if, then, else, for, while, do, etc.
- **Operatory logiczne:** and, or, not
- **Operatory arytmetyczne:** div, mod, ←, ≤, ≥
- **Funkcje I/O:** read, write
- **Komentarze:** // tekst
- **Stringi:** "tekst"
- **Liczby:** 123, 3.14
- **Tablice:** A[i], A[i, j]

### Testy
Otwórz `DEMO_SNIPPETS.md` aby zobaczyć kolorowanie w akcji.

---

## 🔍 Tasks (Zadania)

### Dostępne Tasks:

1. **Waliduj bieżący plik**
   - Skrót: `Ctrl+Shift+B`
   - Waliduje otwarty plik `zadanie.md`

2. **Waliduj wszystkie pliki**
   - Skrót: `Ctrl+Alt+V`
   - Waliduje wszystkie 32 zadania

3. **Waliduj listę 1/2/3**
   - Skróty: `Ctrl+Alt+1/2/3`
   - Waliduje konkretną listę

### Uruchomienie Ręczne
1. `Ctrl+Shift+P`
2. "Tasks: Run Task"
3. Wybierz task

---

## 🐛 Troubleshooting

### Snippety nie działają

**Sprawdź:**
1. Czy jesteś w bloku ` ```pseudocode `?
2. Czy naciskasz Tab po skrócie?
3. Czy plik ma rozszerzenie `.md`?

**Rozwiązanie:**
- Zrestartuj VS Code
- Sprawdź czy plik `pseudocode.code-snippets` istnieje

### Brak kolorowania

**Sprawdź:**
1. Czy używasz bloku ` ```pseudocode `?
2. Czy plik jest w `lista_*/*/zadanie.md`?

**Rozwiązanie:**
- Zrestartuj VS Code
- Sprawdź czy plik `pseudocode.tmLanguage.json` istnieje

### Tasks nie działają

**Sprawdź:**
1. Czy Python jest zainstalowany? `python --version`
2. Czy validator działa? `python validator.py --all`

**Rozwiązanie:**
- Zainstaluj Python 3.11+
- Sprawdź ścieżki w `tasks.json`

---

## 📚 Dokumentacja

- **Główna:** `../PRZEWODNIK_SRODOWISKA.md`
- **Demo:** `../DEMO_SNIPPETS.md`
- **Szablon:** `../SZABLON_ZADANIA.md`
- **Szybki start:** `../QUICK_REFERENCE.md`

---

## ✨ Status

✅ **Gotowe do użycia**

- 6 plików konfiguracyjnych
- 16 snippetów
- 5 tasków
- 5 skrótów klawiszowych
- Pełne podświetlanie składni
- Auto-formatowanie

**Nie wymaga dodatkowej instalacji!**

---

## 🎉 Quick Start

1. Otwórz: `code .`
2. Edytuj: `lista_X/Y_nazwa/zadanie.md`
3. Wpisz: `alg` + Tab
4. Waliduj: `Ctrl+Shift+B`

**Miłego kodowania!** 🚀
