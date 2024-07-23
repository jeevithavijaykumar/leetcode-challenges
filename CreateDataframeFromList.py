""" 2877. Create a DataFrame from List"""
"""Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students."""

import pandas as pd

def createDataframe(student_data):
    result = pd.DataFrame(student_data, columns=['student_id','age'])
    return(result)
