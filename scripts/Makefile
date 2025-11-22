# Makefile dla projektu Pseudokod
# Uproszczone polecenia do zarządzania projektem

.PHONY: help validate validate-all validate-l1 validate-l2 validate-l3 new-task clean install

# Domyślne polecenie - pokaż pomoc
help:
	@echo "=================================="
	@echo "  PSEUDOKOD - DOSTĘPNE POLECENIA"
	@echo "=================================="
	@echo ""
	@echo "  make validate       - Waliduj wszystkie pliki"
	@echo "  make validate-l1    - Waliduj listę 1"
	@echo "  make validate-l2    - Waliduj listę 2"
	@echo "  make validate-l3    - Waliduj listę 3"
	@echo "  make new-task       - Utwórz nowe zadanie (interaktywnie)"
	@echo "  make install        - Zainstaluj zależności"
	@echo "  make clean          - Usuń pliki tymczasowe"
	@echo "  make help           - Pokaż tę pomoc"
	@echo ""

# Walidacja wszystkich plików
validate:
	@echo "🔍 Walidacja wszystkich plików..."
	@python validator.py --all

validate-all: validate

# Walidacja listy 1
validate-l1:
	@echo "🔍 Walidacja listy 1..."
	@python validator.py lista_1/*/zadanie.md

# Walidacja listy 2
validate-l2:
	@echo "🔍 Walidacja listy 2..."
	@python validator.py lista_2/*/zadanie.md

# Walidacja listy 3
validate-l3:
	@echo "🔍 Walidacja listy 3..."
	@python validator.py lista_3/*/zadanie.md

# Utwórz nowe zadanie
new-task:
	@python new_task.py

# Instalacja zależności
install:
	@echo "📦 Instalacja zależności..."
	@pip install -r requirements.txt

# Czyszczenie plików tymczasowych
clean:
	@echo "🧹 Czyszczenie plików tymczasowych..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@find . -type f -name ".DS_Store" -delete 2>/dev/null || true
	@echo "✅ Wyczyszczono"
