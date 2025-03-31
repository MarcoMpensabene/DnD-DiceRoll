import random
import re

def parse_dice_notation(dice_notation: str) -> tuple:
    """Interpreta una stringa nel formato 'NdM' o 'NdM+bonus' e restituisce (N, M, bonus)."""
    try:
        # Usa una regex per trovare il formato NdM con eventuale modificatore +n
        match = re.match(r"(\d+)d(\d+)(\+\d+)?", dice_notation.strip())

        if not match:
            raise ValueError("Formato non valido. Usa 'NdM' o 'NdM+n'.")

        Ndice, Nface = int(match.group(1)), int(match.group(2))
        bonus = int(match.group(3)[1:]) if match.group(3) else 0  # Se esiste il modificatore, rimuove il '+'

        if Ndice <= 0 or Nface <= 1:
            raise ValueError("Il numero di dadi deve essere maggiore di 0 e il numero di facce maggiori di 1.")

        return (Ndice, Nface, bonus)

    except ValueError as e:
        print(f"Errore: {e}")  # Mostriamo l'errore senza bloccare il programma
        return None  # Indichiamo che il parsing è fallito

def roll_dice_with_bonus(num_dice: int, num_faces: int, bonus: int) -> list:
    """Lancia num_dice dadi con num_faces facce e aggiunge il bonus ad ogni singolo tiro."""
    results = [random.randint(1, num_faces) + bonus for _ in range(num_dice)]  # Bonus aggiunto ad ogni tiro
    return results

if __name__ == "__main__":
    while True:
        dice_notation = input("Inserisci la notazione dei dadi (es. 3d6 o 2d8+3): ").strip()
        parsed_input = parse_dice_notation(dice_notation)

        if parsed_input:
            Ndice, Nface, bonus = parsed_input
            results = roll_dice_with_bonus(Ndice, Nface, bonus)
            print(f"Tiri: {results} | Bonus per tiro: {bonus}")
        else:
            print("Errore nell'input, riprova.")
