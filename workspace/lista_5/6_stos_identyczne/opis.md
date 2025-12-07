````markdown
# Operacje na Stosach - Wyjaśnienie

## Stos (Stack)
Struktura danych typu LIFO (Last In, First Out) - ostatni wchodzi, pierwszy wychodzi.

### Operacje podstawowe
- `PUSH(x)` - dodaj element na szczyt, O(1)
- `POP()` - zdejmij i zwróć element ze szczytu, O(1)
- `EMPTY()` - sprawdź czy stos pusty, O(1)
- `TOP()`/`PEEK()` - zobacz szczyt bez usuwania, O(1)

### Zadanie 4: Podział na parzyste/nieparzyste
**Strategia**: Zdejmuj elementy ze stosu S, sprawdzaj parzystość, wrzucaj na odpowiedni stos.
- Złożoność: O(n) czas, O(n) pamięć

**Zastosowanie**: Filtrowanie danych, klasyfikacja

### Zadanie 5: Odwracanie tekstu
**Strategia**: Wrzuć wszystkie znaki na stos, zdejmuj po kolei.
- Właściwość LIFO automatycznie odwraca kolejność
- Złożoność: O(n) czas, O(n) pamięć

**Zastosowanie**: Palindromy, przetwarzanie wsteczne

### Zadanie 6: Sprawdzanie duplikatów
**Strategia**: Zdejmuj elementy, porównuj z każdym elementem na pomocniczym stosie.
- Złożoność: O(n²) czas, O(n) pamięć
- Alternatywa: użyj hash set → O(n) czas

**Optymalizacja**: Sortuj stos (zadanie 8), potem O(n) sprawdzanie sąsiadów

### Zadanie 7: Sprawdzanie nawiasów
**Strategia**: Klasyczny problem parsowania
1. Napotkaj otwierający → PUSH na stos
2. Napotkaj zamykający → POP i sprawdź czy pasuje para
3. Na końcu stos musi być pusty

**Typy par**: (), [], {}

**Błędy**:
- Zamykający bez otwierającego → stos pusty przy POP
- Zła para → np. ( z ]
- Brakuje zamykających → stos niepusty na końcu

**Złożoność**: O(n) czas, O(n) pamięć

**Zastosowanie**: Kompilatory, parsery, walidacja składni

### Zadanie 8: Sortowanie stosu
**Strategia**: Użyj pomocniczego stosu P jako "posortowanego"
1. Zdejmij element temp ze S
2. Dopóki szczyt P > temp → przerzuć z P do S
3. Wrzuć temp na P
4. Powtarzaj aż S pusty
5. Przerzuć wszystko z P do S

**Złożoność**: O(n²) czas, O(n) pamięć
**Podobne do**: Insertion Sort

### Zadanie 9: Usuwanie minimum z największej głębokości
**Strategia**: 
1. Pierwszy przebieg: znajdź minimum i jego głębokość
2. Drugi przebieg: kopiuj wszystko oprócz tego elementu

**Złożoność**: O(n) czas, O(n) pamięć

## Zalety stosów
✓ Proste operacje O(1)
✓ Łatwa implementacja (tablica lub lista)
✓ Naturalne dla problemów rekurencyjnych
✓ Wymagane w wielu algorytmach

## Wady
✗ Brak dostępu do środkowych elementów
✗ Ograniczony rozmiar (wersja tablicowa)
✗ Tylko od szczytu

## Implementacje stosu
1. **Tablica**: szybkie, stały rozmiar
2. **Lista**: dynamiczny rozmiar, wolniejsze
3. **Dwa stosy w jednej tablicy**: oszczędność pamięci

## Zastosowania stosów
- Wywołania funkcji (call stack)
- Parsowanie wyrażeń
- DFS w grafach
- Undo/Redo
- Nawigacja wstecz (przeglądarki)
- Ewaluacja wyrażeń postfixowych

````
