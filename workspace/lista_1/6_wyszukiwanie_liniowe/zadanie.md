# Wyszukiwanie Liniowe

```pseudocode
algorithm WyszukiwanieLiniowe(A, n, x) {
  read(n, x)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  znaleziono ← false
  pozycja ← -1
  
  for i ← 1 to n do {
    if A[i] = x then {
      znaleziono ← true
      pozycja ← i
      i ← n + 1
    }
  }
  
  if znaleziono then {
    write("Element znaleziony na pozycji: ", pozycja)
  } else {
    write("Element nie znaleziony")
  }
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa
