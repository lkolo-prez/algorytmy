# Potęga - Rekurencyjnie

```pseudocode
algorithm PotegaRekurencyjnie(a, n) {
  read(a, n)
  
  if n < 0 then {
    write("Błąd: n musi być nieujemne")
  } else {
    wynik ← PotegaRek(a, n)
    write(a, "^", n, " = ", wynik)
  }
}

algorithm PotegaRek(a, n) {
  if n = 0 then {
    return 1
  } else {
    return a · PotegaRek(a, n - 1)
  }
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa (stos rekursji)
