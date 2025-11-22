# Tablica Wężykowa (Snake Pattern)

```pseudocode
algorithm TablicaWezyk(A, n) {
  read(n)
  
  liczba ← 1
  
  for i ← 1 to n do {
    if i mod 2 = 1 then {
      for j ← 1 to n do {
        A[i, j] ← liczba
        liczba ← liczba + 1
      }
    } else {
      for j ← n to 1 step -1 do {
        A[i, j] ← liczba
        liczba ← liczba + 1
      }
    }
  }
  
  for i ← 1 to n do {
    for j ← 1 to n do {
      write(A[i, j], " ")
    }
    write("\n")
  }
}
```

Złożoność: O(n²) czasowa, O(n²) pamięciowa
