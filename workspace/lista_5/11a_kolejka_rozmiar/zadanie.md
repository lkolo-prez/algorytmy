````markdown
# Kolejka - Liczenie Elementów

```pseudocode
algorithm LiczElementyKolejki(K) {
  if K.EMPTY() == 1 then {
    write("Kolejka pusta, rozmiar = 0")
    return 0
  }
  
  licznik ← 0
  P ← NowyQueue()
  
  while K.EMPTY() == 0 do {
    element ← K.GET()
    P.PUT(element)
    licznik ← licznik + 1
  }
  
  while P.EMPTY() == 0 do {
    K.PUT(P.GET())
  }
  
  write("Rozmiar kolejki: ", licznik)
  return licznik
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa

````
