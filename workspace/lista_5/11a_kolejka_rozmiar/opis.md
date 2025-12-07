````markdown
# Operacje na Kolejkach - Wyjaśnienie

## Kolejka (Queue)
Struktura danych typu FIFO (First In, First Out) - pierwszy wchodzi, pierwszy wychodzi.

### Operacje podstawowe
- `PUT(x)` / `ENQUEUE(x)` - dodaj element na koniec, O(1)
- `GET()` / `DEQUEUE()` - zdejmij element z początku, O(1)
- `EMPTY()` - sprawdź czy kolejka pusta, O(1)

## Zadanie 11a: Liczenie elementów
**Strategia**: 
1. Zdejmuj elementy zliczając je
2. Odkładaj na pomocniczą kolejkę
3. Przerzuć z powrotem

**Złożoność**: O(n) czas, O(n) pamięć

**Optymalizacja**: Przechowuj rozmiar jako pole → O(1)

## Zadanie 11b: Sprawdzanie wartości
**Strategia**:
1. Zdejmuj elementy, sprawdzaj wartość
2. Odkładaj na pomocniczą kolejkę (zachowanie kolejności!)
3. Przerzuć z powrotem

**Złożoność**: O(n) czas, O(n) pamięć

**Uwaga**: Kolejka zostaje niezmieniona (side-effect free)

## Zadanie 12: Implementacje hybrydowe

### Kolejka przez dwa stosy
**Idea**: Dwa stosy S1 (wejście) i S2 (wyjście)

**ENQUEUE(x)**:
- PUSH x na S1
- O(1)

**DEQUEUE()**:
- Jeśli S2 pusty → przerzuć wszystko z S1 do S2
- POP z S2
- **Amortyzowana**: O(1)
- **Najgorsza**: O(n)

**Przykład**:
```
ENQUEUE(1): S1=[1], S2=[]
ENQUEUE(2): S1=[2,1], S2=[]
ENQUEUE(3): S1=[3,2,1], S2=[]

DEQUEUE(): 
  S2 pusty → przerzuć
  S1=[], S2=[1,2,3]
  POP z S2 → zwróć 1
  S1=[], S2=[2,3]

DEQUEUE():
  S2 nie pusty
  POP z S2 → zwróć 2
  S1=[], S2=[3]
```

**Zalety**: Amortyzowana O(1), oszczędność pamięci
**Wady**: Najgorsza O(n)

### Stos przez dwie kolejki
**Idea**: Dwie kolejki Q1 i Q2

**PUSH(x)**:
- PUT x do Q1
- O(1)

**POP()**:
- Przerzuć wszystkie oprócz ostatniego z Q1 do Q2
- GET ostatni z Q1 (to jest szczyt stosu!)
- Zamień Q1 ↔ Q2
- **Zawsze O(n)**

**Przykład**:
```
PUSH(1): Q1=[1], Q2=[]
PUSH(2): Q1=[1,2], Q2=[]
PUSH(3): Q1=[1,2,3], Q2=[]

POP():
  Przerzuć 1,2 do Q2: Q1=[3], Q2=[1,2]
  GET z Q1 → zwróć 3
  Zamień: Q1=[1,2], Q2=[]
  
POP():
  Przerzuć 1 do Q2: Q1=[2], Q2=[1]
  GET z Q1 → zwróć 2
  Zamień: Q1=[1], Q2=[]
```

**Zalety**: Działa
**Wady**: POP zawsze O(n) - **bardzo nieefektywne**

**Alternatywa - jedna kolejka**:
```
PUSH(x):
  n ← rozmiar Q
  PUT x do Q
  Przerzuć n elementów z przodu na tył
  O(n)

POP():
  GET z Q
  O(1)
```

Lepsze gdy częściej POP niż PUSH.

## Porównanie implementacji

| Struktura | Operacje | Kompleksowość | Praktyczność |
|-----------|----------|---------------|--------------|
| **Kolejka normalna** | ENQUEUE/DEQUEUE | O(1)/O(1) | ✓✓✓ |
| **Kolejka 2 stosy** | ENQUEUE/DEQUEUE | O(1)/O(1)* | ✓✓ |
| **Stos normalny** | PUSH/POP | O(1)/O(1) | ✓✓✓ |
| **Stos 2 kolejki** | PUSH/POP | O(1)/O(n) | ✗ |

*amortyzowana

## Zastosowania kolejek
- **Kolejki zadań** (job queues)
- **BFS w grafach**
- **Bufory** (producer-consumer)
- **Kolejki priorytetowe** (z modyfikacją)
- **Round-robin scheduling**
- **Cache** (LRU)

## Implementacje kolejki
1. **Tablica kołowa** (circular buffer): najlepsze O(1)
2. **Lista jednokierunkowa**: O(1) z tail pointer
3. **Dwa stosy**: O(1) amortyzowana, ciekawe akademicko

## Dlaczego uczymy się implementacji hybrydowych?
1. **Zrozumienie struktur**: Jak różne struktury się uzupełniają
2. **Analiza amortyzowana**: Kolejka 2 stosy to klasyczny przykład
3. **Wywiady**: Popularne pytanie na rozmowach o pracę
4. **Kreatywność**: Pokazuje alternatywne myślenie

## Ciekawostki
1. **Deque** (double-ended queue): może działać jako stos I kolejka
2. **Priority queue**: kolejka z priorytetami (zwykle kopiec)
3. **Circular buffer**: bardzo efektywne w embedded systems

````
