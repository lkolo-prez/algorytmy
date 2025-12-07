````markdown
# Sortowanie przez Scalanie

```pseudocode
algorithm Scal(A, lewy, srodek, prawy) {
  n1 ← srodek - lewy + 1
  n2 ← prawy - srodek
  
  for i ← 1 to n1 do {
    L[i] ← A[lewy + i - 1]
  }
  
  for j ← 1 to n2 do {
    R[j] ← A[srodek + j]
  }
  
  i ← 1
  j ← 1
  k ← lewy
  
  while i <= n1 and j <= n2 do {
    if L[i] <= R[j] then {
      A[k] ← L[i]
      i ← i + 1
    } else {
      A[k] ← R[j]
      j ← j + 1
    }
    k ← k + 1
  }
  
  while i <= n1 do {
    A[k] ← L[i]
    i ← i + 1
    k ← k + 1
  }
  
  while j <= n2 do {
    A[k] ← R[j]
    j ← j + 1
    k ← k + 1
  }
}

algorithm SortowaniePrzezScalanie(A, lewy, prawy) {
  if lewy < prawy then {
    srodek ← (lewy + prawy) / 2
    SortowaniePrzezScalanie(A, lewy, srodek)
    SortowaniePrzezScalanie(A, srodek + 1, prawy)
    Scal(A, lewy, srodek, prawy)
  }
}

algorithm MergeSort(A, n) {
  read(n)
  
  for i ← 1 to n do {
    read(A[i])
  }
  
  SortowaniePrzezScalanie(A, 1, n)
  
  write("Posortowana tablica:")
  for i ← 1 to n do {
    write(A[i], " ")
  }
}
```

Złożoność: O(n log n) czasowa (zawsze), O(n) pamięciowa

````
