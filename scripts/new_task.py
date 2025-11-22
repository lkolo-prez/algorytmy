#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator Nowego Zadania - Pseudokod
Automatycznie tworzy strukturę katalogu i plików dla nowego zadania
"""

import os
import sys
from pathlib import Path

SZABLON_ZADANIE = """# {nazwa}

```pseudocode
algorithm {nazwa_algorytmu}({parametry}) {{
  // Wczytanie danych
  read(n)
  
  // Główna logika
  
  
  // Wypisanie wyniku
  write("Wynik = ", wynik)
}}
```

**Złożoność:** O(n)

**Opis:**
{opis}
"""

SZABLON_OPIS = """# {nazwa} - Wyjaśnienie

## 📋 Treść Zadania

{tresc}

## 🎯 Analiza Problemu

### Co Trzeba Zrobić?


### Jak To Zrobić?


### Jakich Struktur Użyć?


## 💡 Rozwiązanie

### Algorytm Krok po Kroku

1. **Wczytanie danych**
   
2. **Przetwarzanie**
   
3. **Wypisanie wyniku**
   

### Przykład Działania

**Dane wejściowe:**
```
n = 5
A = [3, 1, 4, 1, 5]
```

**Dane wyjściowe:**
```
Wynik = ...
```

## ⏱️ Złożoność

- **Czasowa:** O(n)
- **Pamięciowa:** O(n)

## 🔍 Testowanie

### Test 1
**Input:** 
**Output:** 
**✅ Oczekiwane:** 

### Test 2
**Input:** 
**Output:** 
**✅ Oczekiwane:** 

## 📝 Notatki


"""


def normalize_name(name: str) -> str:
    """Normalizuj nazwę dla katalogów i algorytmów"""
    # Usuń polskie znaki
    replacements = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    for pl, en in replacements.items():
        name = name.replace(pl, en)
    return name


def to_camel_case(name: str) -> str:
    """Konwertuj nazwę na CamelCase dla nazwy algorytmu"""
    words = name.replace('_', ' ').split()
    return ''.join(word.capitalize() for word in words)


def create_task(lista: int, numer: str, nazwa: str, nazwa_pelna: str = None, 
                parametry: str = "A, n", tresc: str = "", opis_krotki: str = ""):
    """
    Utwórz nową strukturę zadania
    
    Args:
        lista: Numer listy (1, 2, 3)
        numer: Numer zadania (np. "1", "2a", "3b")
        nazwa: Nazwa zadania (np. "suma_elementow")
        nazwa_pelna: Pełna nazwa do wyświetlenia (opcjonalne)
        parametry: Parametry algorytmu (default: "A, n")
        tresc: Treść zadania dla opis.md
        opis_krotki: Krótki opis do zadanie.md
    """
    if nazwa_pelna is None:
        nazwa_pelna = nazwa.replace('_', ' ').capitalize()
    
    # Normalizuj nazwy
    nazwa = normalize_name(nazwa)
    katalog_nazwa = f"{numer}_{nazwa}"
    
    # Ścieżka katalogu
    katalog_path = Path(f"lista_{lista}") / katalog_nazwa
    
    # Sprawdź czy katalog już istnieje
    if katalog_path.exists():
        print(f"❌ Katalog {katalog_path} już istnieje!")
        return False
    
    # Utwórz katalog
    katalog_path.mkdir(parents=True, exist_ok=True)
    print(f"✅ Utworzono katalog: {katalog_path}")
    
    # Utwórz zadanie.md
    nazwa_algorytmu = to_camel_case(nazwa)
    zadanie_content = SZABLON_ZADANIE.format(
        nazwa=nazwa_pelna,
        nazwa_algorytmu=nazwa_algorytmu,
        parametry=parametry,
        opis=opis_krotki if opis_krotki else f"Algorytm {nazwa_pelna.lower()}"
    )
    
    zadanie_path = katalog_path / "zadanie.md"
    with open(zadanie_path, 'w', encoding='utf-8') as f:
        f.write(zadanie_content)
    print(f"✅ Utworzono plik: {zadanie_path}")
    
    # Utwórz opis.md
    opis_content = SZABLON_OPIS.format(
        nazwa=nazwa_pelna,
        tresc=tresc if tresc else "TODO: Dodaj treść zadania"
    )
    
    opis_path = katalog_path / "opis.md"
    with open(opis_path, 'w', encoding='utf-8') as f:
        f.write(opis_content)
    print(f"✅ Utworzono plik: {opis_path}")
    
    print(f"\n🎉 Zadanie {lista}.{numer} - {nazwa_pelna} utworzone pomyślnie!")
    print(f"📝 Edytuj: {zadanie_path}")
    print(f"📖 Wyjaśnienie: {opis_path}")
    
    return True


def interactive_mode():
    """Tryb interaktywny - zadawaj pytania użytkownikowi"""
    print("="*60)
    print("  📝 GENERATOR NOWEGO ZADANIA - PSEUDOKOD")
    print("="*60)
    print()
    
    # Lista
    while True:
        try:
            lista = int(input("Numer listy (1, 2, 3): "))
            if lista in [1, 2, 3]:
                break
            print("❌ Wybierz 1, 2 lub 3")
        except ValueError:
            print("❌ Podaj liczbę!")
    
    # Numer zadania
    numer = input("Numer zadania (np. 1, 2a, 10): ").strip()
    if not numer:
        print("❌ Numer nie może być pusty!")
        return
    
    # Nazwa (dla katalogu)
    nazwa = input("Nazwa zadania (np. suma_elementow, binary_search): ").strip()
    if not nazwa:
        print("❌ Nazwa nie może być pusta!")
        return
    
    # Nazwa pełna (do wyświetlenia)
    nazwa_pelna = input(f"Pełna nazwa [{nazwa.replace('_', ' ').title()}]: ").strip()
    if not nazwa_pelna:
        nazwa_pelna = nazwa.replace('_', ' ').title()
    
    # Parametry algorytmu
    parametry = input("Parametry algorytmu [A, n]: ").strip()
    if not parametry:
        parametry = "A, n"
    
    # Krótki opis
    opis_krotki = input("Krótki opis (opcjonalnie): ").strip()
    
    print()
    print("📋 Podsumowanie:")
    print(f"  Lista: {lista}")
    print(f"  Numer: {numer}")
    print(f"  Nazwa: {nazwa}")
    print(f"  Pełna nazwa: {nazwa_pelna}")
    print(f"  Parametry: {parametry}")
    print()
    
    potwierdzenie = input("Utworzyć zadanie? (t/n): ").strip().lower()
    if potwierdzenie in ['t', 'tak', 'y', 'yes']:
        create_task(lista, numer, nazwa, nazwa_pelna, parametry, "", opis_krotki)
    else:
        print("❌ Anulowano")


def main():
    """Główna funkcja"""
    if len(sys.argv) == 1:
        # Tryb interaktywny
        interactive_mode()
    elif len(sys.argv) >= 4:
        # Tryb z argumentami: python new_task.py <lista> <numer> <nazwa> [nazwa_pelna] [parametry]
        lista = int(sys.argv[1])
        numer = sys.argv[2]
        nazwa = sys.argv[3]
        nazwa_pelna = sys.argv[4] if len(sys.argv) > 4 else None
        parametry = sys.argv[5] if len(sys.argv) > 5 else "A, n"
        
        create_task(lista, numer, nazwa, nazwa_pelna, parametry)
    else:
        print("Użycie:")
        print("  python new_task.py  # Tryb interaktywny")
        print("  python new_task.py <lista> <numer> <nazwa> [nazwa_pelna] [parametry]")
        print()
        print("Przykład:")
        print("  python new_task.py 1 10 suma_elementow \"Suma Elementów Tablicy\" \"A, n\"")


if __name__ == "__main__":
    main()
