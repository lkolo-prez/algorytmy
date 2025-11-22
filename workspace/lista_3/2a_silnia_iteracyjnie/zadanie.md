# Silnia - Iteracyjnie

```pseudocode
algorithm SilniaIteracyjnie(n) {
  read(n)
  
  if n < 0 then {
    write("Błąd: n nie może być ujemne")
  } else {
    silnia ← 1
    
    for i ← 1 to n do {
      silnia ← silnia · i
    }
    
    write(n, "! = ", silnia)
  }
}
```

Złożoność: O(n) czasowa, O(1) pamięciowa
