""""Problem 175 - Combine Two Tables """

import pandas as pd

def combine_two_tables(person, address):
    combineddf = pd.merge(person,address, on='personId',how='left')
    resultdf = combineddf[['firstName','lastName','city','state']]
    return(resultdf)



