regles = [
    {"conditions": ["fievre", "toux"], "conclusion": "grippe"},
    {"conditions": ["grippe", "douleurs_thoraciques"], "conclusion": "infection_respiratoire"},
    {"conditions": ["infection_respiratoire", "essoufflement"], "conclusion": "hospitalisation_conseillée"},
]

def chainage_avant(faits_initiaux, regles):
    faits = [f.lower() for f in faits_initiaux]
    faits = list(dict.fromkeys(faits))
    applied = True
    trace = []
    while applied:
        applied = False
        for regle in regles:
            conditions = [c.lower() for c in regle["conditions"]]
            conclusion = regle["conclusion"].lower()
            if all(cond in faits for cond in conditions) and conclusion not in faits:
                faits.append(conclusion)
                applied = True
                trace.append((conditions, conclusion))
    if trace:
        print("Règles appliquées (ordre d'application) :")
        for i, (conds, concl) in enumerate(trace, 1):
            print(f"  {i}) SI {' ET '.join(conds)} ALORS {concl}")
    else:
        print("Aucune règle n'a été appliquée.")
    print("Faits finaux :", faits)
    print("-" * 50)
    return faits

def peut_on_deduire(fait_cible, faits_initiaux, regles):
    fait_cible_norm = fait_cible.lower()
    faits_finaux = chainage_avant(faits_initiaux, regles)
    if fait_cible_norm in faits_finaux:
        print(f"Oui, '{fait_cible}' est déduit.")
        return True
    else:
        print(f"Non, le système ne peut pas conclure '{fait_cible}'.")
        return False
