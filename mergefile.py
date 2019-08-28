#This program performs different Merge operations on CSV file
"""Basic script to merge 2 CSV files"""
import numpy as np
import pandas as pd
import os

def filemerge():
    A = str(input("Enter left csv filename\n"))
    A = A + '.csv'

    exists = os.path.isfile(A)

    if exists:
        df1 = pd.read_csv(A ,encoding = 'unicode_escape')
    else:
        print("File doesnt exists..Enter again")
        filemerge()
    while True:
        B = str(input("Enter right csv filename\n"))
        B = B + '.csv'
        exists = os.path.isfile(B)
        if exists:
            df2 = pd.read_csv(B, encoding='unicode_escape')
            break
        else:
            print("Invalid file")
            continue
    ##df2 = pd.read_csv(B ,encoding = 'unicode_escape')
    col = str(input("Enter Column for Merge\n"))
    type = str(input("Enter inner,left,right,outer\n"))
    result = df1.merge(df2, on=col, how=type)
    result.to_csv('merge.csv', index=False)
    print("Files sucessfully merged as merge.csv")

filemerge()
