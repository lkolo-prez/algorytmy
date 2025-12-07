````markdown
# Lista Jednokierunkowa - Przeszukiwanie

```pseudocode
algorithm PrzeszukajListe(lista, wartosc) {
  read(wartosc)
  
  if lista == NULL then {
    write("Lista pusta")
    return 0
  }
  
  aktualny ← lista
  pozycja ← 1
  
  while aktualny != NULL do {
    if aktualny->item == wartosc then {
      write("Znaleziono ", wartosc, " na pozycji ", pozycja)
      return pozycja
    }
    aktualny ← aktualny->next
    pozycja ← pozycja + 1
  }
  
  write("Nie znaleziono ", wartosc)
  return 0
}
```

Złożoność: O(n) czasowa, O(1) pamięciowa

````
