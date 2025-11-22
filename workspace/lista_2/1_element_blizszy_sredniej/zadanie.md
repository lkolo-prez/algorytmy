# Element Najbliższy Średniej

```pseudocode
algorithm ElementBlizszySpodniej(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  suma ← 0
  for i ← 1 to n do {
    suma ← suma + A[i]
  }
  
  srednia ← suma / n
  
  min_roznica ← |A[1] - srednia|
  indeks ← 1
  
  for i ← 2 to n do {
    roznica ← |A[i] - srednia|
    if roznica < min_roznica then {
      min_roznica ← roznica
      indeks ← i
    }
  }
  
  write("Element najbliższy średniej: ", A[indeks], " na pozycji: ", indeks)
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa
