"""this python program will give general stats associated with csv file """



import pandas as pd
import numpy as np

def filestats():
	A = str(input("Enter csv filename\n"))
	A = A + '.csv'
	df = pd.read_csv(A ,encoding = 'unicode_escape')
	##print("Sample records in file are:\n")
	##print(df.head(5))
	print("Total rows are {} and columns are {}".format(df.shape[0],df.shape[1]))
	NanValuePerc = round((df.isnull().sum() / df.shape[0]) * 100, 2)
	print(" ____________________________________")
	print("  Null value percentage columnwise")
	print("#____________________________________#")
	print(NanValuePerc)
	print(" ____________________________________")
	print("    Columns and thier datatype")
	print("#____________________________________#")
	for i in df.columns:
		print("{}: {}".format(i,df[i].dtype))
	

filestats()
