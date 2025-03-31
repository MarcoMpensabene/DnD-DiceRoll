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

def create_character():
    """Permette all'utente di creare un nuovo personaggio."""
    name = input("Inserisci il nome del personaggio: ").strip()
    
    if not name:
        print("Nome non valido.")
        return

    stats = {}
    for stat in ["Forza", "Destrezza", "Costituzione", "Intelligenza", "Saggezza", "Carisma"]:
        while True:
            try:
                value = int(input(f"Inserisci il valore per {stat}: "))
                stats[stat] = value
                break
            except ValueError:
                print("Errore: Inserisci un numero valido.")

    save_character(name, stats)
    print(f"Personaggio '{name}' salvato con successo!")

if __name__ == "__main__":
    print("Vuoi creare un nuovo personaggio? (sì/no)")
    choice = input("> ").strip().lower()
    if choice == "sì" or choice == "si":
        create_character()