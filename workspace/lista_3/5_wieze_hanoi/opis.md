# Wieże Hanoi - Wyjaśnienie

## Opis
Problem Wież Hanoi: przenieść n krążków z pręta źródłowego na pręt docelowy, korzystając z pręta pomocniczego. Reguła: nie można położyć większego krążka na mniejszy.

## Dane Wejściowe
- **n**: liczba krążków

## Wynik
Sekwencja ruchów przenoszenia krążków

## Strategi Rekurencyjna
1. Przenieś n-1 krążków ze źródła na pomocniczy (używając celu)
2. Przenieś największy krążek ze źródła na cel
3. Przenieś n-1 krążków z pomocniczego na cel (używając źródła)

## Przykład n=3
```
Przenieś krążek z 1 na 2
Przenieś krążek z 1 na 3
Przenieś krążek z 2 na 3
Przenieś krążek z 1 na 2
Przenieś krążek z 3 na 1
Przenieś krążek z 3 na 2
Przenieś krążek z 1 na 2
(7 ruchów = 2^3 - 1)
```

## Zastosowania
- Klasyczny problem rekursji
- Teoria algorytmów
- Edukacja

## Uwagi
- **Liczba ruchów**: dokładnie 2^n - 1
- **Złożoność**: O(2^n) - wykładnicza
- **Legenda**: opowie że mnie świat się skończy gdy mnisi przeniosą 64 krążki
- **Niema iteracyjnego rozwiązania**: rekursja jest naturalna dla tego problemu
