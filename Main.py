# Main script for the risk game

# Import classes
from Game import Game
import pandas as pd

# Read the game setup data
card_list = pd.read_csv("Input/Traditional/cards.csv", sep=";")

risk_game = Game(cards=card_list)

