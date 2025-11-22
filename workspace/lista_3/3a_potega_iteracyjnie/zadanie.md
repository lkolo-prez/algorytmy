# Potęga - Iteracyjnie

```pseudocode
algorithm PotegaIteracyjnie(a, n) {
  read(a, n)
  
  if n < 0 then {
    write("Błąd: n musi być nieujemne")
  } else {
    wynik ← 1
    
    for i ← 1 to n do {
      wynik ← wynik · a
    }
    
    write(a, "^", n, " = ", wynik)
  }
}
```

Złożoność: O(n) czasowa, O(1) pamięciowa
