import random
import time

class Game:
    def __init__(self, home_team, away_team, date, home_score=0, away_score=0):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.home_score = home_score
        self.away_score = away_score
        self.time_remaining = 90  # 90-minute game

    def __repr__(self):
        return f"{self.date}: {self.home_team} {self.home_score} - {self.away_score} {self.away_team}"
    
    def winner(self):
        if self.home_score > self.away_score:
            return self.home_team
        elif self.away_score > self.home_score:
            return self.away_team
        return "Draw"

    def play(self):
        print(f"\n🏁 Starting game: {self.home_team} vs {self.away_team}")
        
        while self.time_remaining > 0:
            time.sleep(0.1)  # simulate time passing (can remove or speed up)
            acting_team = random.choice([self.home_team, self.away_team])
            scorer = random.choice(acting_team.players)
            success = random.random() < 0.1  # 10% chance to score

            print(f"{self.time_remaining} min left - {scorer.name} from {acting_team.name} shoots!")

            if success:
                if acting_team == self.home_team:
                    self.home_score += 1
                else:
                    self.away_score += 1
                print(f"⚽ GOAL! {scorer.name} scores for {acting_team.name}!")

            self.time_remaining -= 5  # simulate 5-minute chunks

        print("\n🏁 Final whistle!")
        print(self)
        print("🏆 Winner:", self.winner())