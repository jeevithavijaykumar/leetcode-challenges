""" 2884. Modify Columns """
""" A company intends to give its employees a pay rise.
Write a solution to modify the salary column by multiplying each salary by 2. """

import pandas as pd

def modifySalaryColumn(employees):
    employees['salary']= employees['salary']*2
    return employees
