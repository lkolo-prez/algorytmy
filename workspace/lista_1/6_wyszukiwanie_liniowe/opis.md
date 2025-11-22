# Wyszukiwanie Liniowe - Wyjaśnienie

## Opis
Wyszukiwanie liniowe to najprostszy algorytm wyszukiwania. Polega na przeglądaniu tablicy element po elemencie aż do znalezienia szukanej wartości lub końca tablicy.

## Dane Wejściowe
- **n**: liczba elementów tablicy (n > 0)
- **A[1..n]**: tablica n liczb (może być nieuposortowana)
- **x**: szukana wartość

## Wynik
- **pozycja**: indeks znalezionego elementu (lub -1 jeśli nie znaleziono)
- Komunikat o wyniku wyszukiwania

## Strategia Rozwiązania

### Kroki Algorytmu
1. Wczytaj n, x i elementy tablicy A
2. Zainicjalizuj `znaleziono ← false` i `pozycja ← -1`
3. Przeglądaj tablicę od 1 do n
4. Jeśli A[i] = x, ustaw `znaleziono ← true`, `pozycja ← i` i przerwij pętlę
5. Wypisz wynik

## Przykład

### Dane Wejściowe
```
n = 6
x = 25
A = [10, 25, 30, 5, 25, 15]
```

### Przebieg Algorytmu
| i | A[i] | A[i] = 25? | Akcja |
|---|------|-----------|-------|
| 1 | 10 | nie | kontynuuj |
| 2 | 25 | tak | znaleziono! pozycja = 2 |

### Wynik
```
Element znaleziony na pozycji: 2
```

## Zastosowania
- Wyszukiwanie w nieuposortowanych danych
- Pierwsza implementacja wyszukiwania
- Gdy tablica jest mała
- Gdy struktura danych nie pozwala na sortowanie

## Uwagi
- **Najgorszego przypadku**: gdy element jest na końcu lub go nie ma (O(n) porównań)
- **Średniego przypadku**: O(n/2) porównań
- **Najlepszego przypadku**: O(1) gdy element jest pierwszy
- **Duplikaty**: algorytm zwraca pozycję pierwszego znalezionego elementu
- **Optymalizacja**: dla sortowanych danych użyj wyszukiwania binarnego
