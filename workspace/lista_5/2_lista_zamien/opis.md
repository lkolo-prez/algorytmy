````markdown
# Zamiana Sąsiednich Elementów w Liście - Wyjaśnienie

## Opis
Zamiana dwóch sąsiednich węzłów p i p->next w liście jednokierunkowej wymaga ostrożnej manipulacji wskaźnikami. Operacja zmienia kolejność dwóch elementów bez tworzenia nowych węzłów.

## Strategia
1. Znajdź węzeł poprzedzający p (jeśli p nie jest głową)
2. Zapisz referencje do p i p->next
3. Zaktualizuj wskaźniki:
   - `p->next = p->next->next`
   - `p_next->next = p`
   - Jeśli poprzedni istnieje: `poprzedni->next = p_next`
   - Jeśli p jest głową: `lista = p_next`

## Diagram
```
Przed:  poprz → [p] → [p->next] → dalej
Po:     poprz → [p->next] → [p] → dalej
```

## Złożoność
- **Czasowa**: O(n) - potrzeba znaleźć węzeł poprzedni
- **Pamięciowa**: O(1) - tylko zmienne pomocnicze

## Przypadki specjalne
- p == NULL → błąd
- p->next == NULL → brak zamiany (p jest ostatnim)
- p to głowa listy → nowa głowa to p->next
- Lista ma tylko 2 elementy → zamiana głowy i ogona

## Zastosowania
- Sortowanie bąbelkowe na listach
- Naprawianie kolejności w liście
- Algorytmy na listach (swap adjacent nodes)

````
