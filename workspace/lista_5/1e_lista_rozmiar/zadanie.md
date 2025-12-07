````markdown
# Lista Jednokierunkowa - Liczenie Elementów

```pseudocode
algorithm LiczElementy(lista) {
  if lista == NULL then {
    write("Lista pusta, rozmiar = 0")
    return 0
  }
  
  licznik ← 0
  aktualny ← lista
  
  while aktualny != NULL do {
    licznik ← licznik + 1
    aktualny ← aktualny->next
  }
  
  write("Rozmiar listy: ", licznik)
  return licznik
}
```

Złożoność: O(n) czasowa, O(1) pamięciowa

````
