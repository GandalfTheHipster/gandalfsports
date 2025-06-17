#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py
"""
import sys
import logging
import random
from colorama import init, Fore, Style

import player
import coach
from team import Team
from game import Game

# Configure basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    init()
    #logging.info("Application started.")

    p1 = player.Player("Lebron James", "SF")
    p2 = player.Player("Steph Curry", "PG")
    p3 = player.Player("Noah Edge", "C")
    p4 = player.Player("Aleksa Kvrgic", "PF")

    c1 = coach.Coach("Gregg Popovich")
    c2 = coach.Coach("Kyle Taplin")

    team1 = Team("NBA All-Stars", "LIGHTBLUE_EX", players=[p1, p2], coach=[c1])
    team2 = Team("Fremantle Flamingos", "LIGHTMAGENTA_EX", players=[p3, p4], coach=[c2])

    # Team 1
    team1.pregame_setup()

    # Team 2
    team2.pregame_setup()

    print("\n")
    print(f"{Fore.GREEN}Game Log:{Style.RESET_ALL}")

    game = Game(home_team=team1, away_team=team2, date="2025-01-01")

    game.play()

    #logging.info("Application finished.")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning("Application interrupted by user.")
        sys.exit(0)
    except Exception as e:
        logging.exception("An unhandled exception occurred:")
        sys.exit(1)