import { Database } from "bun:sqlite";

const db = new Database("../npcs.sqlite");

// Ved bruk av Javascript's mer sofistikert object system, kan vi bruke en objekt-orientert metode for å lage denne funksjonen, som gir bedre samling av data og gjør koden enklere en vis vi bruker en vanlig funksjon.
export const multiplier = { // Objektet som holder styr på multiplikatoren
    active: false,
    value: 1,
    count: 0,
    
    activate(value, count) {
        this.active = true;
        this.value = value;
        this.count = count;
    }
};

export class Player { // Klassen for spilleren
    gold: number; // Vi bruker TypeScript, som krever "class properties" som spesifiserer hva slags data som skal lagres i objektet, dette er fordi TypeScript er et statisk språk og trenger å vite hva slags data som skal lagres i objektet. Hvis vi ikke definerer hva slags data som skal lagres, vil TypeScript gi en feilmelding. Dette er ikke et problem i vanlig Javascript eller Python.
    happiness: number;
    
    constructor(gold: number, happiness: number) {
        this.gold = gold;
        this.happiness = happiness;
    }
}

export class NPC { // Klassen for NPCer
    name: string;
    message: string;
    wealthchangeaccept: number;
    happinesschangeaccept: number;
    wealthchangedecline: number;
    happinesschangedecline: number;

    constructor(name, message, wealthchangeaccept, happinesschangeaccept, wealthchangedecline, happinesschangedecline) {
        this.name = name;
        this.message = message;
        this.wealthchangeaccept = wealthchangeaccept;
        this.happinesschangeaccept = happinesschangeaccept
        this.wealthchangedecline = wealthchangedecline;
        this.happinesschangedecline = happinesschangedecline;
    }
}

export function newRound(happiness, gold) { // Funksjonen som kjører en ny runde
    let random_npc = db.query(`SELECT * FROM interactions ORDER BY RANDOM() LIMIT 1`).get(); // Velger en tilfeldig NPC fra databasen
    let npc = new NPC(random_npc.name, random_npc.message, random_npc.wealthchangeaccept, random_npc.happinesschangeaccept, random_npc.wealthchangedecline, random_npc.happinesschangedecline); // Lager et nytt NPC objekt med tilfeldig dataen vi nettopp hentet fra databasen
    console.log(npc.name + ": " + npc.message); // Skriver ut en melding fra NPCen
    console.log("Accepting will result in " + npc.happinesschangeaccept + " happiness and " + npc.wealthchangeaccept + " gold.");
    console.log("Declining will result in " + npc.happinesschangedecline + " happiness and " + npc.wealthchangedecline + " gold.");
};