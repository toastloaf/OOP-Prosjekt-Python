// Importer alle klasser og metoder fra data.ts og sqlite fra Bun (krever at du bruker Bun, fungerer ikke med node.js)
import { multiplier, Player, NPC } from "./data";
import { Database } from "bun:sqlite";

const db = Database.open("npcs.sqlite"); // Opprett en ny database med filnavn "npcs.sqlite"

let player = new Player(100, 100); // Opprett et nytt Player objekt med 100 gold og 100 happiness

console.log(db.query("SELECT * FROM interactions WHERE id = 5").get());