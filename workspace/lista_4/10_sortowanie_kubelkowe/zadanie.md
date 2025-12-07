````markdown
# Sortowanie Kubełkowe

```pseudocode
algorithm SortowanieBabelkoweKubelka(B, rozmiar) {
  for i ← 1 to rozmiar - 1 do {
    for j ← 1 to rozmiar - i do {
      if B[j] > B[j + 1] then {
        temp ← B[j]
        B[j] ← B[j + 1]
        B[j + 1] ← temp
      }
    }
  }
}

algorithm SortowanieKubelkowe(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  liczba_kubelkow ← n
  
  for i ← 0 to liczba_kubelkow - 1 do {
    rozmiar_kubelka[i] ← 0
  }
  
  max_val ← A[1]
  min_val ← A[1]
  
  for i ← 2 to n do {
    if A[i] > max_val then {
      max_val ← A[i]
    }
    if A[i] < min_val then {
      min_val ← A[i]
    }
  }
  
  zakres ← max_val - min_val + 1
  
  for i ← 1 to n do {
    idx ← ((A[i] - min_val) * liczba_kubelkow) / zakres
    if idx == liczba_kubelkow then {
      idx ← idx - 1
    }
    rozmiar_kubelka[idx] ← rozmiar_kubelka[idx] + 1
    Kubelki[idx][rozmiar_kubelka[idx]] ← A[i]
  }
  
  for i ← 0 to liczba_kubelkow - 1 do {
    if rozmiar_kubelka[i] > 0 then {
      SortowanieBabelkoweKubelka(Kubelki[i], rozmiar_kubelka[i])
    }
  }
  
  idx ← 1
  for i ← 0 to liczba_kubelkow - 1 do {
    for j ← 1 to rozmiar_kubelka[i] do {
      A[idx] ← Kubelki[i][j]
      idx ← idx + 1
    }
  }
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n + k) czasowa średnia, O(n²) pesymistyczna, O(n + k) pamięciowa

````
