# teams.py

from classes.team import Team
from classes.player import Player
from classes.coach import Coach

# Create players
p1 = Player("Lebron James", "SF")
p2 = Player("Steph Curry", "PG")
p3 = Player("Noah Edge", "C")
p4 = Player("Aleksa Kvrgic", "PF")

# Create coaches
c1 = Coach("Gregg Popovich")
c2 = Coach("Kyle Taplin")

# Create teams
teams = [
    Team("PER","Perth Mellowkittens", "RED", players=[p1, p2], coach=[c1]),
    Team("ADE","Adelaide 38ers", "CYAN", players=[p1, p2], coach=[c1]),
    Team("MEL","Melbourne Fragented", "BLUE", players=[p1, p2], coach=[c1]),
    Team("SEM","South East Melbourne Orders", "LIGHTGREEN_EX", players=[p1, p2], coach=[c1]),
    Team("BRI","Brisbane Duttons", "YELLOW", players=[p1, p2], coach=[c1]),
    Team("CAI","Cairns Snakes", "LIGHTYELLOW_EX", players=[p1, p2], coach=[c1]),
    Team("NZB","New Zealand Builders", "LIGHTMAGENTA_EX", players=[p1, p2], coach=[c1]),
    Team("SIN","Singapore Slingers", "MAGENTA", players=[p1, p2], coach=[c1])
]

'''
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, and LIGHTWHITE_EX.
'''