// Ved bruk av Javascript's mer sofistikert object system, kan vi bruke en objekt-orientert metode for å lage denne funksjonen, som gir bedre samling av data og gjør koden enklere en vis vi bruker en vanlig funksjon.
export const multiplier = {
    active: false,
    value: 1,
    count: 0,
    
    activate(value, count) {
        this.active = true;
        this.value = value;
        this.count = count;
    }
};

export class Player {
    gold: number; // Vi bruker TypeScript, som krever "class properties" som spesifiserer hva slags data som skal lagres i objektet, dette er fordi TypeScript er et statisk språk og trenger å vite hva slags data som skal lagres i objektet. Hvis vi ikke definerer hva slags data som skal lagres, vil TypeScript gi en feilmelding. Dette er ikke et problem i vanlig Javascript eller Python.
    happiness: number;
    
    constructor(gold: number, happiness: number) {
        this.gold = gold;
        this.happiness = happiness;
    }
}

export class NPC {
    messages: string[]; // Hvor vi lagrer listen av meldinger som NPCen kan si
    wealthchange: number;
    happinesschange: number;

    constructor(messages, wealthchange, happinesschange) {
        this.messages = messages;
        this.wealthchange = wealthchange;
        this.happinesschange = happinesschange;
    }
}

export const Robot = new NPC(["I am a robot", "Beep boop"], 0, 0);

console.log(Robot.messages[Math.floor(Math.random() * Robot.messages.length)]);