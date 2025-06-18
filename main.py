#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
main.py
"""
import sys
import logging
import random
from colorama import init, Fore, Style
from state.teams import teams
from classes.game import Game

# Configure basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logging.basicConfig(level=logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")

SHOWLOG = True

def main():
    init()
    #logging.info("Application started.")

    random_team_indices = random.sample(range(len(teams)), 2)

    #Choose Random Teams
    team1 = teams[random_team_indices[0]]
    team2 = teams[random_team_indices[1]]

    team1.pregame_setup()
    team2.pregame_setup()

    print("\n")
    print(f"{Fore.GREEN}Game Log:{Style.RESET_ALL}")

    game = Game(home_team=team1, away_team=team2, date="2025-01-01")

    if SHOWLOG == False:
        game.play(False)
    else:
        game.play(True)

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