import random

class Player:
    def __init__(self, gold, happiness):
        self.gold = gold
        self.happiness = happiness

class npc:
    def __init__(self, message, wealthchange, happinesschange):
        self.message = message
        self.wealthchange = wealthchange
        self.happinesschange = happinesschange

class Robot(npc):
    msgs = "RobotMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class Warrior(npc):
    msgs = "WarriorMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class Scientist(npc):
    msgs = "ScientistMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class Orc(npc):
    msgs = "OrcMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class Parrot(npc):
    msgs = "ParrotMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class Dragon(npc):
    msgs = "DragonMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class Mouse(npc):
    msgs = "MouseMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class ConstructionWorker(npc):
    msgs = "ConstructionWorkerMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class Farmer(npc):
    msgs = "FarmerMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class Wizard(npc):
    msgs = "WizardMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class FriendlyWitch(npc):
    msgs = "FriendlyWitchMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
class Devil(npc):
    msgs = "DevilMsgs"
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)
# AI-Genererte liste av NPC meldinger
RobotMsgs = [
"Robot| Beep bloop whir! My circuits require an upgrade, 10 gold please.| -10| 0| 1| -1",
"Robot| Boop beep! Scanning... Kingdom defenses low, donate 5 gold for repairs.| -5| 0| 0| -4",
"Robot| Whirr click! Oil reserves depleted. Urgent need for 5 gold.| -5| 0| 1| -1",
"Robot| Clank whizz! Energy levels critical. Requesting 1 gold for charging station.| -1| 0| 0| -1"
]

WarriorMsgs = [
"Warrior| My liege, my sword needs mending. Grant me 5 gold.| -5| 0| 0| -1",
"Warrior| Your Majesty, bandits threaten the realm! We need 10 gold for supplies.| -10| 0| 5| -5",
"Warrior| Sire, the city guard requires new armor. 25 gold is needed.| -25| 0| 20| -20",
"Warrior| Your Grace, I request 5 gold to train new recruits.| -5| 0| 3| -3",
"Warrior| King, our defenses are weak. We need 50 gold for reinforcements.| -50| 0| 40| -5"
]

ScientistMsgs = [
"Scientist| Your Majesty, We need 15 gold to complete my research on crop growth.| -15| 0| 5| 0",
"Scientist| Your Majesty, here are some of our profits from the last research project.| 100| 0| 0| 0",
"Scientist| My liege, grant us 20 gold to research a cure for the plague.| -20| 0| 30| -10",
"Scientist| Your Majesty, 15 gold will fund our research into new building materials.| -15| 0| 0| 0"
]

OrcMsgs = [
"Orc| Raargh! Gold! Need gold! Me want 5 shiny gold!| -5| 0| 1| -1",
"Orc| Grrr! Hungry! Gold for food! Me need 10 gold for boar!| -10| 0| 1| -1",
"Orc| Smash! Need new club! Gold! Me want 5 gold for big club!| -5| 0| 1| -1",
"Orc| Roar! Tribe need gold! Give! Me need 15 gold for tribe!| -15| 0| 5| -1",
"Orc| Graagh! Shiny gold make me strong! Me need 10 gold for strength potion!| -10| 0| 1| -1"
]

ParrotMsgs = [
"Parrot| Squawk! Pretty bird needs shiny gold! Polly wants gold!| -1| 0| 1| -1",
"Parrot| Chirp! Seeds expensive! Need gold! Polly wants 2 gold for seeds!| -2| 0| 1| -1",
"Parrot| Squawk! New perch! Gold please! Polly wants 5 gold for new perch!| -5| 0| 1| -1",
"Parrot| Squawk! Shiny mirror! Need gold! Polly wants 5 gold for a mirror!| -5| 0| 1| -1"
]

DragonMsgs = [
"Dragon| Rumbles {Gold. Bring shiny.}| -10| 0| 0| -10",
"Dragon| Roars {Tribute. Or burn.}| -40| 0| 0| -30",
"Dragon| Snarls {Need. Gold. Now.}| -50| 0| 0| -10",
"Dragon| Puffs smoke {Hoard incomplete. Gold required.}| -20| 0| 30| -30",
"Dragon| Growls {Shiny. Must have. Gold.}| -10| 0| 0| -10"
]

MouseMsgs = [
"Mouse| Squeak squeak... Need cheese...| -1| 0| 1| -1",
"Mouse| Eek! Cat! Need to hide!| -1| 0| 1| -1",
"Mouse| Squeak... Need 5 gold for nest...| -5| 0| 1| -1",
"Mouse| Scurry scurry... Need 10 gold for new home...| -10| 0| 2| -2"
]

ConstructionWorkerMsgs = [
"Construction Worker| Your highness, 10 gold for stronger city walls?| -10| 0| 15| -5",
"Construction Worker| Your Majesty, 15 gold to repair the damaged bridge?| -15| 0| 10| -3",
"Construction Worker| Your Grace, 5 gold to improve the town's roads?| -5| 0| 5| -1",
"Construction Worker| My liege, 20 gold to build a new marketplace?| -20| 0| 40| -20",
"Construction Worker| Your Highness, 10 gold to reinforce the castle walls?| -10| 0| 5| -5"
]

FarmerMsgs = [
"Farmer| Your Majesty, 5 gold for new seeds would be a blessing.| -5| 0| 2| -1",
"Farmer| My liege, 10 gold would help repair our aging tools.| -10| 0| 4| -2",
"Farmer| Your Grace, we need 15 gold to protect our crops from pests.| -15| 0| 6| -3",
"Farmer| Your Highness, 5 gold could buy a new plow horse.| -5| 0| 2| -1",
"Farmer| King, 10 gold would help irrigate our fields.| -10| 0| 4| -2"
]

WizardMsgs = [
"Wizard| By your leave, sire, 15 gold for a potent spell component.| -15| 0| 5| -5",
"Wizard| Your Majesty, 10 gold to enhance the kingdom's magical defenses.| -10| 0| 20| -20",
"Wizard| My liege, 5 gold for research into new enchantments.| -5| 0| 1| -1",
"Wizard| Your Grace, 20 gold for a ritual to improve crop yields.| -20| 0| 10| 0",
"Wizard| Sire, 15 gold to dispel a curse upon the land.| -15| 0| 10| -5"
]

FriendlyWitchMsgs = [
"Friendly Witch| Dearest king, 5 gold for rare herbs, please?| -5| 0| 0| 0",
"Friendly Witch| Your Majesty, 10 gold for a charm to protect the kingdom?| -10| 0| 5| -2",
"Friendly Witch| Sweet king, 5 gold for a potion to boost morale?| -5| 0| 2| 0",
"Friendly Witch| Good king, 15 gold for a ritual to bless the harvest?| -15| 0| 8| -3",
"Friendly Witch| Kind king, 10 gold for ingredients for a healing salve?| -10| 0| 4| -1",
]

DevilMsgs = [
"Devil| If you want, i can steal from the nearby town and give you the profits! what do you say?| 150| 0| -100| 0",
"Devil| May i feast off of your kingdom's happiness? ill pay you handsomely for it!| 200| 0| -150| 0",
]

def random_npc():
    npc_list = [Robot, Warrior, Scientist, Orc, Parrot, Dragon, Mouse, ConstructionWorker, Farmer, Wizard, FriendlyWitch, Devil] # Liste med NPC klassene som skal brukes i spillet.
    selected_npc = random.choice(npc_list)
    #print("selected npc", selected_npc) # Debug funksjon
    selected_msg = random.choice(globals()[selected_npc.msgs]) # Finn hvilken liste av meldinger som skal brukes, og bruk globals() for å si til python at det er en global variabel som tilhører en liste.
    #print("selected msg", selected_msg) # Debug funksjon
    return selected_msg

def gen_npc():
    npcresponse = random_npc()
    npc_message = npcresponse.split("|")[1]
    #print("bruh moment", npcresponse) # Debug funksjon
    npc_name = npcresponse.split("|")[0]
    #print("npc name", npc_name) # Debug funksjon

    # Konverter tallstrenger til heltall
    wealthchange = (int(npcresponse.split("|")[2]), int(npcresponse.split("|")[3]))
    happinesschange = (int(npcresponse.split("|")[4]), int(npcresponse.split("|")[5]))

    # Lag NPC objektet med de riktige navn, meldingen og endringene i gold og happiness
    return npc_name, npc_message, wealthchange, happinesschange
