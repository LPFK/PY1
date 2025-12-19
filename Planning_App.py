from datetime import datetime, time
from typing import List, Dict, Optional, Tuple
import json

class Evenement:
    def __init__(self, titre: str, date: str, heure_debut: str, heure_fin: str, salle: Optional[str] = None):
        self.titre = titre
        self.date = date
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.salle = salle
        self.participants = []

        def __str__(self):
            salle_info = f", Salle: {self.salle}" if self.salle else ""
            participants_info = f", Participants: {', '.join(self.participants)}" if self.participants else ""
            return f"Événement: {self.titre} | Date: {self.date} de {self.heure_debut} à {self.heure_fin}{salle_info}{participants_info}"

            def to_dict(self):
                return {
                    "titre": self.titre,
                    "date": self.date,
                    "heure_debut": self.heure_debut,
                    "heure_fin": self.heure_fin,
                    "salle": self.salle,
                    "participants": self.participants
                }


class Salle:
    def __init__(self, identifiant: str, capacite: int):
        self.identifiant = identifiant
        self.capacite = capacite

    def __str__(self):
        return f"Salle: {self.identifiant}, Capacité: {self.capacite}"


class PlanningManager:
    def __init__(self):
        self.evenement: list[Evenement] = []
        self.participants: list[str] = []
        self.salles: list[Salle] = []

    def ajouter_evenement(self, titre: str, date: str, heure_debut: str, heure_fin: str,
                          salle: Optional[str] = None) -> bool:

        if not self._validate_date(date):
            print("Date invalide. Utilisez le format YYYY-MM-DD.")
            return False

        if not self._validate_time(heure_debut) or not self._validate_time(heure_fin):
            print("Heure invalide. Utilisez le format HH:MM.")
            return False

        if not self._heures_coherentes(heure_debut, heure_fin):
            print("L'heure de fin doit être après l'heure de début.")
            return False

        if salle and not self._verifier_conflit_salle(date, heure_debut, heure_fin, salle):
            print(f"Conflit de salle pour {salle} à la date et heure spécifiées.")
            return False
        nouvel_evenement = Evenement(titre, date, heure_debut, heure_fin, salle)
        self.evenement.append(nouvel_evenement)
        print(f"Événement {titre} ajouté avec succès.")
        return True

    def afficher_evenements_par_date(self, date: optional[str] = None):