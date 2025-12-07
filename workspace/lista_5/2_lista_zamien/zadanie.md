````markdown
# Lista Jednokierunkowa - Zamiana Elementów p i p->next

```pseudocode
algorithm ZamienPNastepny(lista, p) {
  if lista == NULL then {
    write("Lista pusta")
    return NULL
  }
  
  if p == NULL or p->next == NULL then {
    write("Nie mozna zamienic")
    return lista
  }
  
  aktualny ← lista
  poprzedni ← NULL
  
  while aktualny != NULL and aktualny != p do {
    poprzedni ← aktualny
    aktualny ← aktualny->next
  }
  
  if aktualny == NULL then {
    write("Nie znaleziono wezla p")
    return lista
  }
  
  pierwszy ← p
  drugi ← p->next
  
  pierwszy->next ← drugi->next
  drugi->next ← pierwszy
  
  if poprzedni == NULL then {
    lista ← drugi
  } else {
    poprzedni->next ← drugi
  }
  
  write("Zamieniono elementy")
  return lista
}
```

Złożoność: O(n) czasowa, O(1) pamięciowa

````
