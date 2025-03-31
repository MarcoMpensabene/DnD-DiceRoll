import random
from character import load_all_characters
from dice import parse_dice_notation, roll_dice_with_bonus




def main():
    # Carichiamo tutti i personaggi disponibili
    characters = load_all_characters()

    if not characters:
        print("Nessuna scheda personaggio trovata. Controlla il file JSON.")
        return

    # Mostriamo i nomi dei personaggi disponibili
    print("Personaggi disponibili:")
    for name in characters.keys():
        print(f"- {name}")

    # L'utente sceglie un personaggio
    chosen_name = input("Seleziona un personaggio digitando il suo nome: ").strip()

    # Recuperiamo la scheda del personaggio scelto
    character = characters.get(chosen_name)

    if not character:
        print("Errore: personaggio non trovato. Riprova.")
        return

    print(f"Personaggio selezionato: {chosen_name}")

    while True:
        # Richiesta input per il lancio dei dadi
        dice_notation = input("\nInserisci la notazione dei dadi (es. 3d6) o 'exit' per uscire: ").strip()
        if dice_notation.lower() == "exit":
            print("Chiusura del programma...")
            break

        parsed_input = parse_dice_notation(dice_notation)

        if parsed_input:
            Ndice, Nface = parsed_input
            
            # Mostriamo le statistiche disponibili e facciamo scegliere una
            print("Statistiche disponibili:", ", ".join(character.keys()))
            chosen_stat = input("A quale statistica vuoi sommare il tiro? ").strip()

            # Recuperiamo il bonus della statistica scelta
            stat_bonus = character.get(chosen_stat, 0)  # Se la statistica non esiste, usa 0
            
            results = roll_dice_with_bonus(Ndice, Nface, stat_bonus)
            print(f"Risultati del lancio (con bonus {stat_bonus} a {chosen_stat}): {results}")
        else:
            print("Errore: notazione non valida, riprova.")

if __name__ == "__main__":
    main()
