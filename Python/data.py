import random
import sqlite3


class Player:
    def __init__(self, gold, happiness):
        self.gold = gold
        self.happiness = happiness


class NPC:
    def __init__(
        self,
        name,
        message,
        wealthchangeaccept,
        wealthchangedecline,
        happinesschangeaccept,
        happinesschangedecline,
    ):
        self.name = name
        self.message = message
        self.wealthchangeaccept = wealthchangeaccept
        self.wealthchangedecline = wealthchangedecline
        self.happinesschangeaccept = happinesschangeaccept
        self.happinesschangedecline = happinesschangedecline


class specialNPC(NPC):  # Spesial NPC som arver fra NPC
    def __init__(
        self,
        name,
        message,
        wealthchangeaccept,
        wealthchangedecline,
        happinesschangeaccept,
        happinesschangedecline,
    ):
        super().__init__(
            name,
            message,
            wealthchangeaccept,
            wealthchangedecline,
            happinesschangeaccept,
            happinesschangedecline,
        )

    def activateMultiplier(self, value):
        # Aktiverer multiplieren
        # Vi vil ikke at den skal multiplisere negative verdier, så vi sjekker om verdien er større enn 0 før vi multipliserer.
        # Hvis den er mindre enn 0, vil den bli ignorert.
        if self.wealthchangeaccept > 0:
            self.wealthchangeaccept *= value
        if self.happinesschangeaccept > 0:
            self.happinesschangeaccept *= value


db = sqlite3.connect("../npcs.sqlite")  # Koble til databasen med sqlite3
cursor = db.cursor()  # Lage en cursor for å utføre SQL-spørringer


def random_npc():
    cursor.execute(
        "SELECT * FROM interactions ORDER BY RANDOM() LIMIT 1"
    )  # Kjører en SQL-spørring for å hente en tilfeldig rad fra databasen
    return cursor.fetchone()  # Returner raden


def handleChoice(npc, gold, happiness):
    # Håndterer valget til spilleren
    # Denne koden er manuelt oversett fra TypeScript versjonen, som er skrevet av Claude og oversatt av meg.
    choice = input("Accept? Y/N: ").lower()
    if choice == "y":
        gold += npc.wealthchangeaccept
        happiness += npc.happinesschangeaccept
        print(f"You accepted the request.")
    else:
        gold += npc.wealthchangedecline
        happiness += npc.happinesschangedecline
        print(f"You declined the request.")
    return gold, happiness


def newRound(gold, happiness): # Rundesystemet for spillet, hvor spilleren får en tilfeldig NPC og må ta et valg
    cursor.execute(
        "SELECT * FROM interactions ORDER BY RANDOM() LIMIT 1"
    )  # Kjører en SQL-spørring for å hente en tilfeldig rad fra databasen
    npc_data = cursor.fetchone()  # Henter raden
    if npc_data[7] == 1:
        special_npc = specialNPC(
            npc_data[1], npc_data[2], npc_data[3], npc_data[4], npc_data[5], npc_data[6]
        )  # Lager en spesial NPC
        multiplier = round(
            random.uniform(1, 3), 1
        )  # Velger en tilfeldig multiplikator mellom 1 og 3 og runder av til 1 desimal for å unngå store floating point tall
        special_npc.activateMultiplier(multiplier)  # Aktiverer multiplikatoren
        print(f"{special_npc.name}: {special_npc.message}")
        print(
            f"This is a special encounter, a multiplier of {multiplier} has been activated. You will receive {special_npc.happinesschangeaccept} happiness and {special_npc.wealthchangeaccept} gold for accepting."
        )
        print(
            f"Declining will result in {special_npc.happinesschangedecline} happiness and {special_npc.wealthchangedecline} gold."
        )
        gold, happiness = handleChoice(special_npc, gold, happiness)
        print(f"You currently have {gold} gold and {happiness} happiness.")
        return gold, happiness
    else:
        npc = NPC(
            npc_data[1], npc_data[2], npc_data[3], npc_data[4], npc_data[5], npc_data[6]
        )
        print(f"{npc.name}: {npc.message}")
        print(
            f"Accepting will result in {npc.happinesschangeaccept} happiness and {npc.wealthchangeaccept} gold."
        )
        print(
            f"Declining will result in {npc.happinesschangedecline} happiness and {npc.wealthchangedecline} gold."
        )
        gold, happiness = handleChoice(npc, gold, happiness)
        print(f"You currently have {gold} gold and {happiness} happiness.")
        return gold, happiness
