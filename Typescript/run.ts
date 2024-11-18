// Importer alle klasser og metoder fra data.ts og sqlite fra Bun (krever at du bruker Bun, fungerer ikke med node.js)
import { Player, NPC , newRound} from "./data";

let player = new Player(100, 100); // Opprett et nytt Player objekt med 100 gold og 100 happiness

console.log("As the king of this kingdom, you must make decisions that will affect the happiness and wealth of the kingdom. People may come to you to ask for your help or to ask for money, you may accept or reject their requests.")
console.log("You have " + player.gold + " gold and " + player.happiness + " happiness.");

while (player.happiness > 0 && player.gold > 0) {
    const [newHappiness, newGold] = newRound(player.happiness, player.gold);
    player.happiness = newHappiness;
    player.gold = newGold;
}

console.log("Game Over! Your kingdom has fallen.");