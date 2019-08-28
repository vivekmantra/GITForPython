"""Basic script to Concat 2 CSV files"""

import numpy as np
import pandas as pd
import os

def fileconcat():
    A = str(input("Enter first csv filename\n"))
    A = A + '.csv'
    df1 = pd.read_csv(A, encoding='unicode_escape')
    B = str(input("Enter second csv filename\n"))
    B = B + '.csv'
    df2 = pd.read_csv(B, encoding='unicode_escape')
    x = int(input("Enter 0 for row-wise, 1 for columnwise concat\n"))
    out = pd.concat([df1,df2], axis=x)
    out.to_csv('concat.csv', index=False)
    print("Files sucessfully merged as concat.csv")

fileconcat()