class FootballPlayer{
    constructor(playerName, position, clubName){
        this.name = playerName;
        this.position = position;
        this.club = clubName;
        this.goalScored = 0;
    }
    scoreGoal(){
        this.goalScored += 1;
        console.log(`ဂိုး!!! ${this.club} အသင်းအတွက် ${this.name} က ဂိုးသွင်းသွားပါပြီး။ စုစုပေါင်းသွင်းဂိုး: ${this.goalScored}`);
    }
    showDetails(){
        console.log(`${this.name} ဟာ ${this.club} အသင်းရဲ့ ${this.position} ကစားသမား ဖြစ်ပါတယ်`);
    }
}
const player1 = new FootballPlayer("Marcus Rashford", "Forward", "Manchester United");
const player2 = new FootballPlayer("Bruno Fernandes", "Midfielder", "Manchester United");
player1.showDetails();
player1.scoreGoal();
player1.scoreGoal();
player2.showDetails();