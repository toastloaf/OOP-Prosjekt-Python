import { Database } from "bun:sqlite";

const db = new Database("../npcs.sqlite");

// Ved bruk av Javascript's mer sofistikert object system, kan vi bruke en objekt-orientert metode for å lage denne funksjonen, som gir bedre samling av data og gjør koden enklere en vis vi bruker en vanlig funksjon.

export class Player {
  // Klassen for spilleren
  gold: number; // Vi bruker TypeScript, som krever "class properties" som spesifiserer hva slags data som skal lagres i objektet, dette er fordi TypeScript er et statisk språk og trenger å vite hva slags data som skal lagres i objektet.
  happiness: number; // Hvis vi ikke definerer hva slags data som skal lagres, vil TypeScript gi en feilmelding. Dette er ikke et problem i vanlig Javascript eller Python.

  constructor(gold: number, happiness: number) {
    this.gold = gold;
    this.happiness = happiness;
  }
}

export class NPC {
  // Klassen for NPCer
  name: string;
  message: string;
  wealthchangeaccept: number;
  happinesschangeaccept: number;
  wealthchangedecline: number;
  happinesschangedecline: number;

  constructor(
    name,
    message,
    wealthchangeaccept,
    happinesschangeaccept,
    wealthchangedecline,
    happinesschangedecline
  ) {
    this.name = name;
    this.message = message;
    this.wealthchangeaccept = wealthchangeaccept;
    this.happinesschangeaccept = happinesschangeaccept;
    this.wealthchangedecline = wealthchangedecline;
    this.happinesschangedecline = happinesschangedecline;
  }
}

export class specialNPC extends NPC {
  // Child-klassen til spesial NPCer (multiplier)
  special: string;

  constructor(
    name,
    message,
    wealthchangeaccept,
    happinesschangeaccept,
    wealthchangedecline,
    happinesschangedecline,
    special
  ) {
    super(
      name,
      message,
      wealthchangeaccept,
      happinesschangeaccept,
      wealthchangedecline,
      happinesschangedecline
    );
    this.special = special;
  }

  activateMultiplier(value) {
    // Aktiverer multiplieren
    // Vi vil ikke at den skal multiplisere negative verdier, så vi sjekker om verdien er større enn 0 før vi multipliserer.
    // Hvis den er mindre enn 0, vil den bli ignorert.
    if (this.wealthchangeaccept > 0) {
      this.wealthchangeaccept *= value;
    }
    if (this.happinesschangeaccept > 0) {
      this.happinesschangeaccept *= value;
    }
  }
}

function handleChoice(
  // Ved hjelp av AI (Claude 3.5 Sonnet), lagde jeg denne funksjonen, slik at vi kan bruke den for både vanlige og spesielle NPCer.
  // Dette gjør koden mer lesbar og enklere å forstå, med en veldig stor reduksjon i antall linjer og repetisjon.
  // Hvis du vil se hvordan koden ser ut uten denne funkjsonen, finner du det i GitHub historikken.
  npc: NPC | specialNPC,
  happiness: number,
  gold: number
): [number, number] {
  let choice = prompt("Accept? Y/N: ");
  if (choice?.toLowerCase() === "y") {
    console.log("You accepted the request.");
    gold += npc.wealthchangeaccept;
    happiness += npc.happinesschangeaccept;
  } else {
    console.log("You declined the request.");
    gold += npc.wealthchangedecline;
    happiness += npc.happinesschangedecline;
  }
  return [happiness, gold];
}

export function newRound(happiness: number, gold: number): [number, number] {
  let random_npc = db
    .query(`SELECT * FROM interactions ORDER BY RANDOM() LIMIT 1`)
    .get();

  if (random_npc.special == "1") {
    let special_npc = new specialNPC(
      random_npc.name,
      random_npc.message,
      random_npc.wealthchangeaccept,
      random_npc.happinesschangeaccept,
      random_npc.wealthchangedecline,
      random_npc.happinesschangedecline,
      random_npc.special
    );
    const multiplier = Math.round((Math.random() * (3 - 1) + 1) * 10) / 10; // Random tall mellom 1 og 3, skrives rart på grunn av avrunding i TypeScript.
    // Runder av til 1 desimal for å unngå store floating point tall.
    special_npc.activateMultiplier(multiplier);

    console.log(`${special_npc.name}: ${special_npc.message}`);
    console.log(
      `This is a special encounter, a multiplier of ${multiplier} has been activated. You will receive ${special_npc.happinesschangeaccept} happiness and ${special_npc.wealthchangeaccept} gold for accepting.`
    );
    console.log(
      `Declining will result in ${special_npc.happinesschangedecline} happiness and ${special_npc.wealthchangedecline} gold.`
    );
    console.log(`You currently have ${gold} gold and ${happiness} happiness.`);

    return handleChoice(special_npc, happiness, gold);
  } else {
    let npc = new NPC(
      random_npc.name,
      random_npc.message,
      random_npc.wealthchangeaccept,
      random_npc.happinesschangeaccept,
      random_npc.wealthchangedecline,
      random_npc.happinesschangedecline
    );

    console.log(`${npc.name}: ${npc.message}`);
    console.log(
      `Accepting will result in ${npc.happinesschangeaccept} happiness and ${npc.wealthchangeaccept} gold.`
    );
    console.log(
      `Declining will result in ${npc.happinesschangedecline} happiness and ${npc.wealthchangedecline} gold.`
    );
    console.log(`You currently have ${gold} gold and ${happiness} happiness.`);

    return handleChoice(npc, happiness, gold);
  }
}
