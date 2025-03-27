def parse_dice_notation(dice_notation: str) -> tuple:
    
    
    
    
    user_input = dice_notation.split('d') # divide l'input in due parti prima e dopo la "d"
    Ndice = int(user_input[0]) # numero dadi
    Nface = int(user_input[1]) #numero facce 
    return (Ndice , Nface) # Restituzione dei valori estratti dall'input utente 

# print(parse_dice_notation("15d20"))  # Output: (3, 6)
# print(parse_dice_notation("1d20")) # Output: (1, 20)
