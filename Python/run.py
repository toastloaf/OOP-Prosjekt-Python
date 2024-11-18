import data

player = data.Player(100, 100)

print("As the king of this kingdom, you must make decisions that will affect the happiness and wealth of the kingdom. People may come to you to ask for your help or to ask for money, you may accept or reject their requests.")
print("You have", player.gold, "gold and", player.happiness, "happiness.")

while True:
    gold, happiness = data.newRound(player.gold, player.happiness)
    player.gold = gold
    player.happiness = happiness
    if player.gold <= 0 or player.happiness <= 0:
        print("Game Over! Your kingdom has fallen.")
        break