# Funkcja F(y,z) - Rosyjski Chłopek

```pseudocode
algorithm FunkcjaFRosyjski(y, z) {
  read(y, z)
  wynik ← FRosyjskiRek(y, z)
  write("F(", y, ",", z, ") = ", wynik)
}

algorithm FRosyjskiRek(y, z) {
  if y = 1 then {
    return z
  } else {
    if y mod 2 = 0 then {
      return FRosyjskiRek(y div 2, z · 2)
    } else {
      return z + FRosyjskiRek(y - 1, z)
    }
  }
}

algorithm FunkcjaFRosyjskiIter(y, z) {
  read(y, z)
  
  wynik ← 0
  
  while y > 0 do {
    if y mod 2 = 1 then {
      wynik ← wynik + z
    }
    
    y ← y div 2
    z ← z · 2
  }
  
  write("Wynik = ", wynik)
}
```

Złożoność: O(log y) czasowa, O(log y) lub O(1) pamięciowa
