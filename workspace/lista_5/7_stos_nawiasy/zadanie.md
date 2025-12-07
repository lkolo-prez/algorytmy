````markdown
# Stos - Sprawdzanie Poprawności Nawiasów

```pseudocode
algorithm SprawdzNawiasy(kod, n) {
  read(n)
  S ← NowyStack()
  
  for i ← 1 to n do {
    read(kod[i])
    
    if kod[i] == '(' or kod[i] == '[' or kod[i] == '{' then {
      S.PUSH(kod[i])
    }
    
    if kod[i] == ')' or kod[i] == ']' or kod[i] == '}' then {
      if S.EMPTY() == 1 then {
        write("Blad: zamykajacy bez otwierajacego")
        return 0
      }
      
      otwarty ← S.POP()
      
      poprawna_para ← 0
      if kod[i] == ')' and otwarty == '(' then {
        poprawna_para ← 1
      }
      if kod[i] == ']' and otwarty == '[' then {
        poprawna_para ← 1
      }
      if kod[i] == '}' and otwarty == '{' then {
        poprawna_para ← 1
      }
      
      if poprawna_para == 0 then {
        write("Blad: niepoprawna para nawiasow")
        return 0
      }
    }
  }
  
  if S.EMPTY() == 0 then {
    write("Blad: brakuje zamykajacych nawiasow")
    return 0
  }
  
  write("Nawiasy poprawne")
  return 1
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa

````
