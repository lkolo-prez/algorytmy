````markdown
# Stos - Usuwanie Najmniejszego z Największej Głębokości

```pseudocode
algorithm UsunMinZGlebokich(A, B) {
  P ← NowyStack()
  min_val ← 999999
  min_glebokość ← 0
  glebokość ← 0
  
  while A.EMPTY() == 0 do {
    element ← A.POP()
    glebokość ← glebokość + 1
    P.PUSH(element)
    
    if element < min_val then {
      min_val ← element
      min_glebokość ← glebokość
    }
    
    if element == min_val and glebokość > min_glebokość then {
      min_val ← element
      min_glebokość ← glebokość
    }
  }
  
  write("Minimum ", min_val, " na glębokosci ", min_glebokość)
  
  glebokość ← 0
  while P.EMPTY() == 0 do {
    element ← P.POP()
    glebokość ← glebokość + 1
    
    if element == min_val and glebokość == min_glebokość then {
      write("Pominieto ", element)
    } else {
      B.PUSH(element)
    }
  }
  
  while B.EMPTY() == 0 do {
    A.PUSH(B.POP())
  }
  
  write("Usunieto najmniejszy element z najglębszej pozycji")
}
```

Złożoność: O(n) czasowa, O(n) pamięciowa

````
