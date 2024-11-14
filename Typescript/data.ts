// Ved bruk av Javascript's mer sofistikert object system, kan vi bruke en objekt-orientert metode for å lage denne funksjonen, som gir bedre samling av data og gjør koden enklere en vis vi bruker en vanlig funksjon.
const multiplier = {
    active: false,
    value: 1,
    count: 0,
    
    activate(value, count) {
        this.active = true;
        this.value = value;
        this.count = count;
    }
};

class Player {
    gold: number; // Vi bruer TypeScript, som krever "class properties" som spesifiserer hva slags data som skal lagres i objektet, dette er fordi TypeScript er et statisk språk og trenger å vite hva slags data som skal lagres i objektet. Hvis vi ikke definerer hva slags data som skal lagres, vil TypeScript gi en feilmelding. Dette er ikke et problem i vanlig Javascript eller Python.
    happiness: number;
    
    constructor(gold: number, happiness: number) {
        this.gold = gold;
        this.happiness = happiness;
    }
}

class NPC {
    message: string;
    wealthchange: number;
    happinesschange: number;

    constructor(message, wealthchange, happinesschange) {
        this.message = message;
        this.wealthchange = wealthchange;
        this.happinesschange = happinesschange;
    }
}

