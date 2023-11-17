heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))

prix_unitaire = float(input("Entrez le prix unitaire d'une heure de travail : "))

if heures_travaillees <= 39:
    montant_total = heures_travaillees * prix_unitaire
elif heures_travaillees <= 44:
    heures_normales = 39
    heures_supplementaires = heures_travaillees - heures_normales
    montant_total = (heures_normales * prix_unitaire) + (heures_supplementaires * prix_unitaire * 1.5)
elif heures_travaillees <= 49:
    heures_normales = 39
    heures_supplementaires_1 = 5
    heures_supplementaires_2 = heures_travaillees - (heures_normales + heures_supplementaires_1)
    montant_total = (heures_normales * prix_unitaire) + (heures_supplementaires_1 * prix_unitaire * 1.5) + (heures_supplementaires_2 * prix_unitaire * 1.75)
else:
    heures_normales = 39
    heures_supplementaires_1 = 5
    heures_supplementaires_2 = 5
    heures_supplementaires_3 = heures_travaillees - (heures_normales + heures_supplementaires_1 + heures_supplementaires_2)
    montant_total = (heures_normales * prix_unitaire) + (heures_supplementaires_1 * prix_unitaire * 1.5) + (heures_supplementaires_2 * prix_unitaire * 1.75) + (heures_supplementaires_3 * prix_unitaire * 2.0)

print(f"Le montant total à payer est : {montant_total} .")