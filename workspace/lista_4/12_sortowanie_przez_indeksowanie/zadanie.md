````markdown
# Sortowanie przez Indeksowanie

```pseudocode
algorithm SortowaniePrzezIndeksowanie(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  for i ← 1 to n do {
    Indeksy[i] ← i
  }
  
  for i ← 1 to n - 1 do {
    for j ← i + 1 to n do {
      if A[Indeksy[i]] > A[Indeksy[j]] then {
        temp ← Indeksy[i]
        Indeksy[i] ← Indeksy[j]
        Indeksy[j] ← temp
      }
    }
  }
  
  write("Posortowana tablica (przez indeksy):")
  for i ← 1 to n do {
    write(A[Indeksy[i]], " ")
  }
  
  write("Tablica indeksów:")
  for i ← 1 to n do {
    write(Indeksy[i], " ")
  }
}
```

Złożoność: O(n²) czasowa, O(n) pamięciowa

````
