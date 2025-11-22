# Rozmiana Kwoty na Monety

```pseudocode
algorithm RozmianaKwoty(kwota) {
  read(kwota)
  
  nominaly[1] ← 25
  nominaly[2] ← 10
  nominaly[3] ← 5
  nominaly[4] ← 1
  
  for i ← 1 to 4 do {
    liczba_monet ← kwota div nominaly[i]
    write("Monet nominału ", nominaly[i], ": ", liczba_monet)
    kwota ← kwota mod nominaly[i]
  }
}
```

Złożoność: O(n) czasowa, O(1) pamięciowa (n = liczba nominałów)
