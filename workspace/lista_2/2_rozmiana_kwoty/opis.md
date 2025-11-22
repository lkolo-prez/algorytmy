# Rozmiana Kwoty na Monety - Wyjaśnienie

## Opis
Algorytm rozwiązuje problem rozmienienia kwoty na minimalną liczbę monet. Wykorzystuje algorytm zachłanny (greedy), który zawsze wybiera największą dostępną monetę. Dla standardowych nominałów gwarantuje wynik optymalny.

## Dane Wejściowe
- **kwota**: kwota do rozmiany (liczba naturalna)
- Nominały: [25, 10, 5, 1] (stałe w algorytmie)

## Wynik
Liczba monet każdego nominału potrzebna do rozmiany

## Strategia Rozwiązania

### Kroki Algorytmu (podejście zachłanne)
1. Wczytaj kwotę
2. Dla każdego nominału od największego do najmniejszego:
   - Podziel kwotę przez nominał (dzielenie całkowite)
   - Wypisz liczbę monet tego nominału
   - Zmniejsz kwotę o rozmienionym: `kwota ← kwota mod nominał`

## Przykład

### Dane Wejściowe
```
kwota = 63
```

### Przebieg Algorytmu
| Krok | Nominał | 63 div nominał | Liczba monet | Reszta (mod) |
|------|---------|---|---|---|
| 1 | 25 | 63 div 25 = 2 | **2 × 25 zł** | 63 mod 25 = 13 |
| 2 | 10 | 13 div 10 = 1 | **1 × 10 zł** | 13 mod 10 = 3 |
| 3 | 5 | 3 div 5 = 0 | **0 × 5 zł** | 3 mod 5 = 3 |
| 4 | 1 | 3 div 1 = 3 | **3 × 1 zł** | 3 mod 1 = 0 |

### Wynik
```
Rozmiana 63 zł:
- Monet nominału 25: 2
- Monet nominału 10: 1
- Monet nominału 5: 0
- Monet nominału 1: 3
Razem: 6 monet
```

## Zastosowania
- Kasy sklepów (rozmiana reszty)
- Bankamaty
- Automaty do wydawania monet
- Systemy płatnicze
- Algorytmy optymalizacyjne

## Uwagi
- **Algorytm zachłanny**: Działa dla standardowych nominałów [1, 5, 10, 25, 50, 100]
- **Nie zawsze optymalny**: Dla nominałów [1, 3, 4] i kwoty 6: zachłanny daje [4,1,1] (3 monety), optymalny [3,3] (2 monety)
- **Dla tego zadania**: Gwarantuje wynik optymalny
- **Przyspieszenie**: Dla dużych kwot można sortować nominały malejąco
