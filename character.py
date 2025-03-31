import json
import os

CHARACTER_FILE = "character.json"

def load_all_characters():
    """Carica tutti i personaggi dal file JSON."""
    if not os.path.exists(CHARACTER_FILE):
        return {}

    try:
        with open(CHARACTER_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Errore nel file JSON, potrebbe essere corrotto.")
        return {}

def save_character(name, stats):
    """Salva un nuovo personaggio o aggiorna un esistente."""
    characters = load_all_characters()
    characters[name] = stats

    with open(CHARACTER_FILE, "w", encoding="utf-8") as file:
        json.dump(characters, file, indent=4)

