# NWD Euklidesa

```pseudocode
algorithm NWDIteracyjnie(a, b) {
  read(a, b)
  
  while b ≠ 0 do {
    temp ← b
    b ← a mod b
    a ← temp
  }
  
  write("NWD = ", a)
}

algorithm NWDRekurencyjnie(a, b) {
  read(a, b)
  wynik ← NWDRek(a, b)
  write("NWD = ", wynik)
}

algorithm NWDRek(a, b) {
  if b = 0 then {
    return a
  } else {
    return NWDRek(b, a mod b)
  }
}
```

Złożoność: O(log min(a,b)) czasowa, O(1) lub O(log min(a,b)) pamięciowa
