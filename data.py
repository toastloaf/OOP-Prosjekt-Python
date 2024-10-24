import random
import os
import google.generativeai as genai

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

def random_npc():
    npc_list = [Robot, Warrior, Scientist, Orc, Parrot, Dragon]
    selected_npc = random.choice(npc_list)
    return selected_npc.__name__  # Return the name of the selected NPC class as a string

genai.configure(api_key=os.getenv("GEMINI_APIKEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="You are the AI model for a video game about a king (player) who has to accept or decline the requests made by NPCs, your job is to create the messages that these NPCs will say to the king, as well as the results of the request being either accepted or declined, you only need six variables for this, which will be passed along to the game code; the NPC to say the message, the message, the wealth change and/or happiness change if the request is accepted, and another one for if the request is declined, and if a value should not change upon either accepting or declining, just type 0 in that field. Heres the formatting you must use: [\"Npcname\", \"ExampleMessage\", \"AcceptedWealthChangeValue\", \"AcceptedHappinessChangeValue\", \"DeclinedWealthChangeValue\", \"DeclinedHappinessChangeValue\"], and PLEASE remember that you can put negative values in any of the fields, so if a request requires the player to pay or give someone gold, just make it negative upon accepting or declining, which means if an npc needs money, make it negative, and if they give money, make it positive, dont forget this. The Npcname will be supplied in the user message and you must ensure that the message and variables you supply to the game actually make a bit of sense in accordance to the Npcname you are given, and make sure to write the messages in a fantasy DnD style, with no more than 20 words in each message. Also any non-human NPCs should act in a way that is fitting for their species and CANNOT speak english, but make sure to add actual text at the end of their message inbetween asterisks, kinda like an internal thouht of what they are saying.",
)

chat_session = model.start_chat(
  history=[
  ]
)
def gen_npc(npcname):
    response = chat_session.send_message(npcname)
    print(response.text)
    message = response.text
    # Extract variables from the AI model's response
    try:
        # Parse the JSON-like string into a Python list
        parsed_response = eval(message)

        # Extract the required variables
        npc_name, npc_message, wealth_change_accept, happiness_change_accept, wealth_change_decline, happiness_change_decline = parsed_response

        # Convert numeric strings to integers
        wealthchange = (int(wealth_change_accept), int(wealth_change_decline))
        happinesschange = (int(happiness_change_accept), int(happiness_change_decline))

        # Update the message to include only the NPC's dialogue
        message = npc_message
    except:
        # If there's an error in parsing, use default values
        print("Error parsing AI response. Using default values.")
        wealthchange = (0, 0)
        happinesschange = (0, 0)
    return npc(message, wealthchange, happinesschange)
