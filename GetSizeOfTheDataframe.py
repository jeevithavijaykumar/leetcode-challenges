""" 2878. Get the Size of a DataFrame"""
""" Write a solution to calculate and display the number of rows and columns of players. """

import pandas as pd

def getDataframeSize(players):
    [row,col]= players.shape
    return([row,col])