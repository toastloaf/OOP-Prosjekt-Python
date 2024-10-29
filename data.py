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
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class Warrior(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class Scientist(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class Orc(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class Parrot(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class Dragon(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class Mouse(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class ConstructionWorker(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class Farmer(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class Wizard(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

class FriendlyWitch(npc):
    def __init__(self, message, wealthchange, happinesschange):
        super().__init__(message, wealthchange, happinesschange)

# AI-Genererte liste av NPC meldinger
RobotMsgs = [
"Robot| Beep bloop whir! My circuits require an upgrade, 10 gold please.| -10| 0| 0| -2",
"Robot| Boop beep! Scanning... Kingdom defenses low, donate 5 gold for repairs.| -5| 2| 0| -2",
"Robot| Whirr click! Oil reserves depleted. Urgent need for 5 gold.| -5| 0| 0| -1",
"Robot| Clank whizz! Energy levels critical. Requesting 10 gold for charging station.| -10| 0| 0| -3"
]

WarriorMsgs = [
"Warrior| My liege, my sword needs mending. Grant me 5 gold.| -5| 0| 0| -1",
"Warrior| Your Majesty, bandits threaten the realm! We need 10 gold for supplies.| -10| 5| 0| -5",
"Warrior| Sire, the city guard requires new armor. 15 gold is needed.| -15| 7| 0| -7",
"Warrior| Your Grace, I request 5 gold to train new recruits.| -5| 3| 0| -3",
"Warrior| King, our defenses are weak. We need 10 gold for reinforcements.| -10| 5| 0| -5"
]

ScientistMsgs = [
"Scientist| Your Majesty, I need 15 gold to complete my research on crop growth.| -15| 10| 0| 0",
"Scientist| Sire, 10 gold will allow me to develop a new sanitation system.| -10| 7| 0| -3",
"Scientist| Your Grace, with 10 gold, I can improve the kingdom's irrigation system.| -10| 7| 0| -3",
"Scientist| My liege, grant me 20 gold to research a cure for the plague.| -20| 15| 0| -10",
"Scientist| Your Majesty, 15 gold will fund my research into new building materials.| -15| 10| 0| -5"
]

OrcMsgs = [
"Orc| Raargh! Gold! Need gold! Me want 5 shiny gold!| -5| 0| 0| -2",
"Orc| Grrr! Hungry! Gold for food! Me need 10 gold for boar!| -10| 0| 0| -3",
"Orc| Smash! Need new club! Gold! Me want 5 gold for big club!| -5| 0| 0| -1",
"Orc| Roar! Tribe need gold! Give! Me need 15 gold for tribe!| -15| 0| 0| -5",
"Orc| Graagh! Shiny gold make me strong! Me need 10 gold for strength potion!| -10| 2| 0| -2"
]

ParrotMsgs = [
"Parrot| Squawk! Pretty bird needs shiny gold! Polly wants 5 gold!| -5| 1| 0| 0",
"Parrot| Chirp! Seeds expensive! Need gold! Polly wants 10 gold for seeds!| -10| 2| 0| -1",
"Parrot| Squawk! New perch! Gold please! Polly wants 5 gold for new perch!| -5| 1| 0| 0",
"Parrot| Squawk! Shiny mirror! Need gold! Polly wants 10 gold for a mirror!| -10| 2| 0| -1"
]

DragonMsgs = [
"Dragon| Rumbles {Gold. Bring shiny.}| -10| 0| 0| -10",
"Dragon| Roars {Tribute. Or burn.}| -15| 0| 0| -20",
"Dragon| Snarls {Need. Gold. Now.}| -5| 0| 0| -5",
"Dragon| Puffs smoke {Hoard incomplete. Gold required.}| -20| 0| 0| -30",
"Dragon| Growls {Shiny. Must have. Gold.}| -10| 0| 0| -10"
]

MouseMsgs = [
"Mouse| Squeak squeak... Need cheese, 5 gold please...| -5| 1| 0| 0",
"Mouse| Eek! Cat! Need 10 gold to hide!| -10| 2| 0| -2",
"Mouse| Squeak... Need 5 gold for nest...| -5| 1| 0| 0",
"Mouse| Scurry scurry... Need 10 gold for new home...| -10| 2| 0| -2"
]

ConstructionWorkerMsgs = [
"Construction Worker| Your highness, 10 gold for stronger city walls?| -10| 5| 0| -2",
"Construction Worker| Your Majesty, 15 gold to repair the damaged bridge?| -15| 7| 0| -3",
"Construction Worker| Your Grace, 5 gold to improve the town's roads?| -5| 3| 0| -1",
"Construction Worker| My liege, 20 gold to build a new marketplace?| -20| 10| 0| -5",
"Construction Worker| Your Highness, 10 gold to reinforce the castle walls?| -10| 5| 0| -2"
]

FarmerMsgs = [
"Farmer| Your Majesty, 5 gold for new seeds would be a blessing.| -5| 2| 0| -1",
"Farmer| My liege, 10 gold would help repair our aging tools.| -10| 4| 0| -2",
"Farmer| Your Grace, we need 15 gold to protect our crops from pests.| -15| 6| 0| -3",
"Farmer| Your Highness, 5 gold could buy a new plow horse.| -5| 2| 0| -1",
"Farmer| King, 10 gold would help irrigate our fields.| -10| 4| 0| -2"
]

WizardMsgs = [
"Wizard| By your leave, sire, 15 gold for a potent spell component.| -15| 5| 0| -5",
"Wizard| Your Majesty, 10 gold to enhance the kingdom's magical defenses.| -10| 7| 0| -3",
"Wizard| My liege, 5 gold for research into new enchantments.| -5| 3| 0| -1",
"Wizard| Your Grace, 20 gold for a ritual to improve crop yields.| -20| 10| 0| -7",
"Wizard| Sire, 15 gold to dispel a curse upon the land.| -15| 8| 0| -5"
]

FriendlyWitchMsgs = [
"Friendly Witch| Dearest king, 5 gold for rare herbs, please?| -5| 3| 0| 0",
"Friendly Witch| Your Majesty, 10 gold for a charm to protect the kingdom?| -10| 5| 0| -2",
"Friendly Witch| Sweet king, 5 gold for a potion to boost morale?| -5| 2| 0| 0",
"Friendly Witch| Good king, 15 gold for a ritual to bless the harvest?| -15| 8| 0| -3",
"Friendly Witch| Kind king, 10 gold for ingredients for a healing salve?| -10| 4| 0| -1",
]

def random_npc():
    npc_list = [Robot, Warrior, Scientist, Orc, Parrot, Dragon, Mouse, ConstructionWorker, Farmer, Wizard, FriendlyWitch]
    selected_npc = random.choice(npc_list)
    print("selected npc", selected_npc)

    if selected_npc == Robot:
        selected_msg = random.choice(RobotMsgs)
    elif selected_npc == Warrior:
        selected_msg = random.choice(WarriorMsgs)
    elif selected_npc == Scientist:
        selected_msg = random.choice(ScientistMsgs)
    elif selected_npc == Orc:
        selected_msg = random.choice(OrcMsgs)
    elif selected_npc == Parrot:
        selected_msg = random.choice(ParrotMsgs)
    elif selected_npc == Dragon:
        selected_msg = random.choice(DragonMsgs)
    elif selected_npc == Mouse:
        selected_msg = random.choice(MouseMsgs)
    elif selected_npc == ConstructionWorker:
        selected_msg = random.choice(ConstructionWorkerMsgs)
    elif selected_npc == Farmer:
        selected_msg = random.choice(FarmerMsgs)
    elif selected_npc == Wizard:
        selected_msg = random.choice(WizardMsgs)
    elif selected_npc == FriendlyWitch:
        selected_msg = random.choice(FriendlyWitchMsgs)
    print("selected msg", selected_msg)
    return selected_msg

def gen_npc():
    npcresponse = random_npc()
    npc_message = npcresponse.split("|")[1]
    print("bruh moment", npcresponse)
    npc_name = npcresponse.split("|")[0]
    print("npc name", npc_name)
    # Convert numeric strings to integers
    wealthchange = (int(npcresponse.split("|")[2]), int(npcresponse.split("|")[3]))
    happinesschange = (int(npcresponse.split("|")[4]), int(npcresponse.split("|")[5]))

    # Create the NPC object with the correct name and message
    return npc(npc_name, npc_message, wealthchange, happinesschange)  # Use npc_name for the name