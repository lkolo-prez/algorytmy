````markdown
# Kolejka - Sprawdzanie Wartości

```pseudocode
algorithm CzyZawieraWartosc(K, szukana) {
  read(szukana)
  
  if K.EMPTY() == 1 then {
    write("Kolejka pusta")
    return 0
  }
  
  znaleziono ← 0
  P ← NowyQueue()
  
  while K.EMPTY() == 0 do {
    element ← K.GET()
    
    if element == szukana then {
      znaleziono ← 1
      write("Znaleziono ", szukana, " w kolejce")
    }
    
    P.PUT(element)
  }
  
  while P.EMPTY() == 0 do {
    K.PUT(P.GET())
  }
  
  if znaleziono == 0 then {
    write("Nie znaleziono ", szukana)
  }
  
  return znaleziono
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa

````
