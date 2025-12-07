````markdown
# Lista Jednokierunkowa - Dodawanie Po Elemencie

```pseudocode
algorithm DodajPo(lista, wartosc, cel) {
  read(wartosc)
  read(cel)
  
  nowy ← NowyWezel(wartosc)
  
  if lista == NULL then {
    write("Lista pusta")
    return NULL
  }
  
  aktualny ← lista
  
  while aktualny != NULL do {
    if aktualny->item == cel then {
      nowy->next ← aktualny->next
      aktualny->next ← nowy
      write("Dodano ", wartosc, " po ", cel)
      return lista
    }
    aktualny ← aktualny->next
  }
  
  write("Nie znaleziono elementu ", cel)
  return lista
}
```

Złożoność: O(n) czasowa, O(1) pamięciowa

````
