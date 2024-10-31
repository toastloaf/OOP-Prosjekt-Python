import data

player = data.Player(100, 100)

print("As the king of this kingdom, you must make decisions that will affect the happiness and wealth of the kingdom. People may come to you to ask for your help or to ask for money, you may accept or reject their requests.")

def play_the_damn_game():
    npc_name, npc_message, wealthchange, happinesschange = data.gen_npc()
    print(f"{npc_name}: {npc_message}")
    print(f"Accepting will result in: {happinesschange[0]} happiness and {wealthchange[0]} gold.")
    print(f"Declining will result in: {happinesschange[1]} happiness and {wealthchange[1]} gold.")
    happiness_change_on_accept = happinesschange[0]
    gold_change_on_accept = wealthchange[0]
    happiness_change_on_decline = happinesschange[1]
    gold_change_on_decline = wealthchange[1]

    #print(f"debug time: {happiness_change_on_accept}, {gold_change_on_accept}, {happiness_change_on_decline}, {gold_change_on_decline}")

    choice = input("Y/N: ").lower()
    if choice == "y":
        print(f"You accepted the request.")
        player.happiness += happiness_change_on_accept
        player.gold += gold_change_on_accept
    else:
        print(f"You declined the request.")
        player.happiness += happiness_change_on_decline
        player.gold += gold_change_on_decline

    print(f"The kingdom's happiness is now {player.happiness} and your gold is now {player.gold}.")

while True:
    play_the_damn_game()
    if player.happiness <= 0 or player.gold <= 0:
        print("You have lost the game, bruh moment.")
        break
