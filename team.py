from colorama import init, Fore, Style
init()


class Team:
    def __init__(self, name, colour, players=None, coach=None):
        self.name = name
        self.players = players if players else []
        self.coach = coach if coach else []
        self.colour = colour

    def __repr__(self):
        color = getattr(Fore, self.colour.upper(), "")
        return f"{color}Team {self.name}{Style.RESET_ALL}"

    def add_player(self, player):
        self.players.append(player)

    def add_coach(self, coach):
        self.players.append(coach)

    def list_players(self):
        print(f"{self.name} PLAYERS:")
        for player in self.players:
            print(player(self.name))
    
    def list_coach(self):
        print(f"{self.name} COACH:")
        for coach in self.coach:
            print(coach)

    def pregame_setup(self):
        print(self)
        print(f"COACH:")
        for coach in self.coach:
            print(coach.name)
        
        print(f"PLAYERS:")
        for player in self.players:
            print(player.name)