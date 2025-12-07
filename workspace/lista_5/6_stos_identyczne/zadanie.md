````markdown
# Stos - Sprawdzanie Identycznych Elementów

```pseudocode
algorithm CzyIdentyczneNaStosieLiniowo(S) {
  if S.EMPTY() == 1 then {
    write("Stos pusty")
    return 0
  }
  
  Spomocniczy ← NowyStack()
  znaleziono ← 0
  
  while S.EMPTY() == 0 do {
    element ← S.POP()
    
    Stemp ← NowyStack()
    while Spomocniczy.EMPTY() == 0 do {
      sprawdzany ← Spomocniczy.POP()
      if sprawdzany == element then {
        znaleziono ← 1
        write("Znaleziono identyczne: ", element)
      }
      Stemp.PUSH(sprawdzany)
    }
    
    while Stemp.EMPTY() == 0 do {
      Spomocniczy.PUSH(Stemp.POP())
    }
    
    Spomocniczy.PUSH(element)
  }
  
  while Spomocniczy.EMPTY() == 0 do {
    S.PUSH(Spomocniczy.POP())
  }
  
  if znaleziono == 0 then {
    write("Brak identycznych elementow")
  }
  
  return znaleziono
}
```

Złożoność: O(n²) czasowa, O(n) pamięciowa

````
