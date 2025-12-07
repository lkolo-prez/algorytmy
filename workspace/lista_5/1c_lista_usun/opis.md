````markdown
# Lista Jednokierunkowa - Operacje Podstawowe - Wyjaśnienie

## Opis
Lista jednokierunkowa to liniowa struktura danych złożona z węzłów, gdzie każdy węzeł zawiera dane (`item`) i wskaźnik do następnego węzła (`next`). Ostatni węzeł wskazuje na `NULL`. Lista pozwala na efektywne dodawanie i usuwanie elementów, ale dostęp do elementu wymaga przejścia przez wszystkie poprzednie.

## Struktura węzła
```
struct node {
  Item item;      // dane
  node *next;     // wskaźnik do następnego
};
```

## Operacje podstawowe

### 1a. Dodawanie przed elementem - O(n)
**Strategia**: Trzeba znaleźć węzeł PRZED zadanym elementem.
- Jeśli cel to pierwszy element → nowy staje się głową
- W przeciwnym razie → przeszukuj aż znajdziesz węzeł, którego `next` wskazuje na cel

**Przypadki specjalne**:
- Lista pusta → błąd
- Element nie istnieje → błąd
- Dodanie przed pierwszym → zmiana głowy listy

### 1b. Dodawanie po elemencie - O(n)
**Strategia**: Znajdź węzeł z zadaną wartością, wstaw nowy za nim.
- Prostsze niż dodawanie przed (nie trzeba śledzić poprzedniego)
- `nowy->next = aktualny->next`
- `aktualny->next = nowy`

**Przypadki specjalne**:
- Lista pusta → błąd
- Element nie istnieje → błąd
- Dodanie po ostatnim → nowy staje się ostatnim

### 1c. Usuwanie elementu - O(n)
**Strategia**: Znajdź węzeł z wartością i usuń go aktualizując wskaźniki.
- Jeśli pierwszy element → zmień głowę
- W przeciwnym razie → `poprzedni->next = aktualny->next`

**Przypadki specjalne**:
- Lista pusta → błąd
- Element nie istnieje → brak akcji
- Usunięcie pierwszego → zmiana głowy
- Usunięcie ostatniego → poprzedni wskazuje NULL

### 1d. Przeszukiwanie - O(n)
**Strategia**: Przejdź przez listę od głowy, porównując każdy element.
- Zwróć pozycję gdy znaleziono
- Zwróć 0 gdy nie znaleziono

**Złożoność**: zawsze O(n) - może trzeba przejść całą listę

### 1e. Liczenie elementów - O(n)
**Strategia**: Przejdź przez całą listę, licząc węzły.
- Inicjalizuj licznik = 0
- Dla każdego węzła: licznik++
- Zwróć licznik

**Alternatywa**: Przechowuj rozmiar jako pole struktury listy (O(1) dostęp)

## Złożoności

| Operacja | Złożoność czasowa | Pamięć |
|----------|-------------------|--------|
| Dodaj przed | O(n) | O(1) |
| Dodaj po | O(n) | O(1) |
| Usuń | O(n) | O(1) |
| Szukaj | O(n) | O(1) |
| Rozmiar | O(n) | O(1) |
| Dodaj na początek | O(1) | O(1) |
| Dodaj na koniec | O(n) lub O(1)* | O(1) |

*O(1) jeśli przechowujemy wskaźnik do ostatniego elementu

## Zalety i Wady list jednokierunkowych

### Zalety
✓ Dynamiczny rozmiar - rośnie/maleje w miarę potrzeb
✓ Efektywne wstawianie/usuwanie na początku O(1)
✓ Nie wymaga ciągłej pamięci (jak tablica)
✓ Łatwa implementacja

### Wady
✗ Brak dostępu losowego - O(n) dla i-tego elementu
✗ Dodatkowa pamięć na wskaźniki
✗ Nie można iść wstecz
✗ Gorsza lokalność cache niż tablice

## Porównanie: Lista vs Tablica

| Cecha | Lista | Tablica |
|-------|-------|---------|
| Dostęp do i-tego | O(n) | O(1) |
| Wstawianie na początek | O(1) | O(n) |
| Wstawianie w środek | O(n) | O(n) |
| Usuwanie | O(n) | O(n) |
| Pamięć | n * (data + ptr) | n * data |
| Rozmiar | Dynamiczny | Stały* |

*w językach z dynamicznymi tablicami może rosnąć

## Zastosowania
- Implementacja stosów i kolejek
- Gdy częste wstawianie/usuwanie na początku
- Gdy rozmiar danych nieznany z góry
- Gdy nie potrzeba dostępu losowego
- Listy sąsiedztwa w grafach

## Optymalizacje

### 1. Lista z ogonem (tail pointer)
```
struct list {
  node *head;
  node *tail;  ← wskaźnik do ostatniego
}
```
Dodawanie na końcu: O(n) → O(1)

### 2. Lista z rozmiarem
```
struct list {
  node *head;
  int size;
}
```
Pobieranie rozmiaru: O(n) → O(1)

### 3. Lista z wartownikiem (sentinel)
```
Dodaj węzeł wartownik na początku (zawsze)
Eliminuje sprawdzanie head == NULL
```

## Typowe błędy
1. **Zgubienie głowy** przy usuwaniu pierwszego
2. **Memory leak** - brak zwalniania usuniętych węzłów
3. **Null pointer** - nie sprawdzanie NULL przed dereferencją
4. **Nieskończona pętla** - zapętlona lista

````
