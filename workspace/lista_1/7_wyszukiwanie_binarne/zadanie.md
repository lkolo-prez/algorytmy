# Wyszukiwanie Binarne

```pseudocode
algorithm WyszukiwanieBinarne(A, n, x) {
  read(n, x)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  lewo ← 1
  prawo ← n
  znaleziono ← false
  pozycja ← -1
  
  while lewo ≤ prawo do {
    srodek ← (lewo + prawo) div 2
    
    if A[srodek] = x then {
      znaleziono ← true
      pozycja ← srodek
      lewo ← prawo + 1
    } else {
      if A[srodek] < x then {
        lewo ← srodek + 1
      } else {
        prawo ← srodek - 1
      }
    }
  }
  
  if znaleziono then {
    write("Element znaleziony na pozycji: ", pozycja)
  } else {
    write("Element nie znaleziony")
  }
}
```

Złożoność: O(log n) czasowa, O(n) pamięciowa
