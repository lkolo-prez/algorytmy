````markdown
# Sortowanie przez Wstrząsanie (Koktajlowe)

```pseudocode
algorithm SortowanieKoktajlowe(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  zamieniono ← 1
  start ← 1
  koniec ← n
  
  while zamieniono == 1 do {
    zamieniono ← 0
    
    for i ← start to koniec - 1 do {
      if A[i] > A[i + 1] then {
        temp ← A[i]
        A[i] ← A[i + 1]
        A[i + 1] ← temp
        zamieniono ← 1
      }
    }
    
    if zamieniono == 0 then {
      break
    }
    
    zamieniono ← 0
    koniec ← koniec - 1
    
    for i ← koniec - 1 downto start do {
      if A[i] > A[i + 1] then {
        temp ← A[i]
        A[i] ← A[i + 1]
        A[i + 1] ← temp
        zamieniono ← 1
      }
    }
    
    start ← start + 1
  }
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n²) czasowa (pesymistyczna), O(n) (optymistyczna), O(1) pamięciowa

````
