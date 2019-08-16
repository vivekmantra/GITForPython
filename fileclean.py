

"""This function is to remove duplicates and Null values from CSV file """



import pandas as pd
import numpy as np

def fileclean():
    A = str(input("Enter csv filename\n"))
    A = A + '.csv'
    df = pd.read_csv(A ,encoding = 'unicode_escape')
    print("Total rows are {} and columns are {}".format(df.shape[0],df.shape[1]))
    duplicateRowsDF = df[df.duplicated()]
    dcount = len(duplicateRowsDF)
    print("Total duplicates in file are: {} rows".format(dcount))
    if dcount != 0:
        ans = str(input(("do you want to remove duplicates(Y/y)?\n")))
        if ans == 'Y' or ans == 'y':
            df = df.drop_duplicates(keep='first')

            print("First occurance of duplicates are retained")
        else:
            print("Duplicates were not removed")
    print("Total Missing Values: {}".format(df.isnull().sum().sum()))
    if (df.isnull().sum().sum()) != 0:
        nullremove = str(input("Do you want to replace Null values in file(Y/y)?\n"))
        if nullremove == 'Y' or nullremove == 'y':
            for i in df.columns:
                ##print(df[i].dtype)
                if df[i].dtype =='object':
                   df[i] = df[i].fillna("Not Available")
                elif df[i].dtype =='float64':
                    check= str(input("Float value.. replace with median or zero?\n"))
                    if check == 'median':
                        value = df[i].median()
                    else:
                        value = 0

                    df[i] = df[i].fillna(value)
                else:
                    df[i] = df[i].fillna(0)


    df.to_csv(A,index=False)

fileclean()

