# LISTA 3 - ZADANIE 4
## Wieże Hanoi (Towers of Hanoi)

### Opis
Klasyczny problem rekurencji: Przenieść n dysków z wieży źródłowej (A) na wieżę docelową (C) przy pomocy wieży pomocniczej (B), przestrzegając reguł:
1. Można przenosić tylko jeden dysk na raz
2. Większy dysk nigdy nie może leżeć na mniejszym dysku
3. Dysków możemy używać tylko jako źródła lub celu, nie jako magazyn pośredni (poza B)

### Wyjaśnienie logiki
1. Aby przenieść n dysków z A na C:
2. Najpierw przenieś n-1 dysków z A na B (używając C jako pomocniczy)
3. Przenieś największy dysk z A na C
4. Przenieś n-1 dysków z B na C (używając A jako pomocniczy)

Przypadek bazowy: Jeśli n=1, przenieś dysk bezpośrednio

### Pseudokod

```
algorithm WiezeHanoi(n, źródło, cel, pomocniczy)
  
  if (n = 1) then
    write("Przenieś dysk z ", źródło, " na ", cel)
  else
    // Przenieś n-1 dysków z źródła na pomocniczy
    WiezeHanoi(n-1, źródło, pomocniczy, cel)
    
    // Przenieś największy dysk ze źródła na cel
    write("Przenieś dysk z ", źródło, " na ", cel)
    
    // Przenieś n-1 dysków z pomocniczego na cel
    WiezeHanoi(n-1, pomocniczy, cel, źródło)
  end if
  
end algorithm

// Program główny
program MAIN
  read(n)
  write("Sekwencja ruchów dla ", n, " dysków:")
  WiezeHanoi(n, "A", "C", "B")
end program
```

---

### Przykład 1: n=1

Jeden dysk, A → C:
```
Przenieś dysk z A na C
```

Razem: **1 ruch**

---

### Przykład 2: n=2

Dwa dyski, A → C:

```
WiezeHanoi(2, A, C, B):
  1. WiezeHanoi(1, A, B, C)
     → Przenieś dysk z A na B
  
  2. Przenieś dysk z A na C
  
  3. WiezeHanoi(1, B, C, A)
     → Przenieś dysk z B na C
```

Sekwencja ruchów:
```
1. Przenieś dysk z A na B (mały)
2. Przenieś dysk z A na C (duży)
3. Przenieś dysk z B na C (mały)
```

Razem: **3 ruchy**

---

### Przykład 3: n=3

Trzy dyski, A → C:

```
WiezeHanoi(3, A, C, B):

  1. WiezeHanoi(2, A, B, C)     // 3 ruchy
     1.1. WiezeHanoi(1, A, C, B)
          → Przenieś dysk z A na C (mały)
     1.2. Przenieś dysk z A na B (średni)
     1.3. WiezeHanoi(1, C, B, A)
          → Przenieś dysk z C na B (mały)
  
  2. Przenieś dysk z A na C (DUŻY)
  
  3. WiezeHanoi(2, B, C, A)     // 3 ruchy
     3.1. WiezeHanoi(1, B, A, C)
          → Przenieś dysk z B na A (mały)
     3.2. Przenieś dysk z B na C (średni)
     3.3. WiezeHanoi(1, A, C, B)
          → Przenieś dysk z A na C (mały)
```

Sekwencja ruchów (7 razem):
```
1. A → C (1)
2. A → B (2)
3. C → B (1)
4. A → C (3 - DUŻY!)
5. B → A (1)
6. B → C (2)
7. A → C (1)
```

Razem: **7 ruchów**

---

### Drzewo rekurencji (n=3)

```
WiezeHanoi(3, A, C, B)
├─ WiezeHanoi(2, A, B, C)
│  ├─ WiezeHanoi(1, A, C, B) → Ruch
│  ├─ Ruch (A→B)
│  └─ WiezeHanoi(1, C, B, A) → Ruch
├─ Ruch (A→C) [DUŻY DYSK]
└─ WiezeHanoi(2, B, C, A)
   ├─ WiezeHanoi(1, B, A, C) → Ruch
   ├─ Ruch (B→C)
   └─ WiezeHanoi(1, A, C, B) → Ruch
```

---

### Potencjalne problemy logiczne

1. **Brak warunku bazowego (n=1)**
   - Problem: `if (n > 1) ...` (nigdy bazowy)
   - Wynik: Nieskończona rekurencja
   - Rozwiązanie: `if (n = 1) write(...)` na początku

2. **Kolejność parametrów w rekurencji**
   - Problem: Zwykłe pomylenie pomocniczy/cel
   - Wynik: Ruchy będą nielogiczne
   - Rozwiązanie: Zawsze: (n-1, źródło, pomocniczy, cel), ruch, (n-1, pomocniczy, cel, źródło)

3. **Brak drukowania głównego ruchu**
   - Problem: Zapomnieni o `write(...)` dla największego dysku
   - Wynik: Sekwencja będzie niekompletna
   - Rozwiązanie: `write(...)` musi być POMIĘDZY dwoma wywołaniami

4. **Parametry podane w złej kolejności**
   - Problem: `WiezeHanoi(n-1, cel, źródło, pomocniczy)` zamiast `(n-1, źródło, pomocniczy, cel)`
   - Wynik: Całkowicie błędne rozwiązanie
   - Rozwiązanie: Zawsze: źródło→cel (pomocniczy ma pomóc!)

5. **Powtórzenie trzeciego kroku zamiast drugiego**
   - Problem: Dwa razy `WiezeHanoi(n-1, pomocniczy, cel, źródło)`
   - Wynik: Dysków nie przeniesie na ostateczne miejsce
   - Rozwiązanie: Drugi krok musi być drukowanie ruchu głównego dysku

### Tablica liczby ruchów

| n | Liczba ruchów | Wzór |
|---|-------|---------|
| 0 | 0 | (nie istnieje) |
| 1 | 1 | 2^1 - 1 |
| 2 | 3 | 2^2 - 1 |
| 3 | 7 | 2^3 - 1 |
| 4 | 15 | 2^4 - 1 |
| 5 | 31 | 2^5 - 1 |
| 10 | 1023 | 2^10 - 1 |
| 20 | 1048575 | 2^20 - 1 |
| 64 | 18446744073709551615 | 2^64 - 1 |

**Legenda:** Liczba ruchów = 2^n - 1

---

### Właściwość matematyczna

```
T(n) = 2×T(n-1) + 1

Rozwiązanie: T(n) = 2^n - 1
```

Dla n=64 (legenda o świątyni): około 18 trylionów ruchów!
Jeśli jeden ruch to 1 sekunda, zajęłoby ~585 miliardów lat!

---

### Złożoność

- **Czasowa: O(2^n)** - liczba ruchów wynosi 2^n - 1
- **Pamięciowa: O(n)** - głębokość stosu rekurencji

Zagrożenie:
- Dla n=30: ~1 miliarda ruchów
- Dla n=64: ~18 trylionów (niemożliwe!)

---

### Zastosowanie

1. **Teoria informatyki:** Przykład sytuacji gdzie brutalna iteracja jest niemożliwa
2. **Nauka rekurencji:** Klasyczny "musi być", wszyscy go uczą
3. **Analiza algorytmów:** Przykład O(2^n) złożoności
4. **Gry i zagadki:** Zagadka sama w sobie
5. **Fizyka:** Alguny modelują problemy używając tego

### Historia

Legenda hindu:
- W świątyni Brahmy jest 64 dyski złota
- Mnisi przesuwają je zgodnie z zasadami
- Kiedy będą gotowi, nastąpi koniec świata!

---

### Iteracyjne rozwiązanie

Istnieje również iteracyjne rozwiązanie, ale jest dużo bardziej skomplikowane.
Rekurencja jest naturalnym sposobem wyrażenia tego problemu.

```
Iteracyjnie: śledź parzyste/nieparzyste dyski, rób legalne ruchy...
Znacznie bardziej zawiłe!
```

### Ćwiczenie

Spróbuj ręcznie rozwiązać n=4:
- Powinno być 15 ruchów
- Zwróć uwagę na symetrię!

### Uwagi

- Jeden z KLASYCZNYCH przykładów rekurencji
- Nie da się iterować do n=64 (2^64 to za dużo)
- Świadczy o mocy rekurencji
- Każde rozwiązanie jest OPTYMALNE (2^n - 1 to minimum)
- Generalnie: jeśli możesz, zawsze przenieś n-1, potem jeden, potem n-1 ponownie!

