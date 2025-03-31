import json

def load_character_data(filename="character.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)  # Carica i dati dal file JSON
    except FileNotFoundError:
        print("Errore: File della scheda non trovato.")
        return None
    except json.JSONDecodeError:
        print("Errore: Il file JSON non è valido.")
        return None
