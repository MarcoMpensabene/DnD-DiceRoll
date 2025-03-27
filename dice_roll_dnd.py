def parse_dice_notation(dice_notation: str) -> tuple:
    try:
        if "d" not in dice_notation:
            raise ValueError("Input non valido , inserire un valore del tipo 'NdM' dove N è il numero di dadi e M il numero di facce")
        user_input = dice_notation.split('d') # divide l'input in due parti prima e dopo la "d"
    
        if len(user_input) != 2:
            raise ValueError("Input non valido , inserir un valore del tipo 'NdM' dove N è il numero di dadi e M il numero di facce")
        Ndice , Nface = int(user_input[0]), int(user_input[1]) # assegna i valori a Ndice e Nface
        if Ndice <= 0 or Nface <= 1:
            raise ValueError("Il numero di dadi deve essere maggiore di 0 e il numero di facce devono essere maggiori di 1")
        return (Ndice , Nface) # Restituzione dei valori estratti dall'input utente
    
    except ValueError as e:
        print(f"Errore: {e}")  # Stampa l'errore senza interrompere il programma
        return None  # Ritorna None in caso di errore
    
    
print(parse_dice_notation("3d20"))

# print(parse_dice_notation("15d20"))  # Output: (3, 6)
# print(parse_dice_notation("1d20")) # Output: (1, 20)
