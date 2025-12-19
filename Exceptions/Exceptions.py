def calculate_moyenne():
    notes = []
    
    print("Entrez vos notes (tapez 'fin' pour terminer)")
    
    while True:
        try:
            entry = input("Note : ")
            if entry.lower() == "fin":
                break
            note = float(entry)
            if note < 0 or note > 20:
                raise ValueError("la note doit etre entre 0 et 20")
            notes.append(note)
        except ValueError as e:
            print(f"Erreur : {e}")
    if len(notes) == 0:
        print("Aucune note entre")
    else: 
        moyenne = sum(notes) / len(notes)
        print(f"Moyenne : {moyenne:.2f}")

calculate_moyenne()
