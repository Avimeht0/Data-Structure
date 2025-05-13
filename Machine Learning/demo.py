import pandas as pd
# how to read a csv file 
df=pd.read_csv("titanic.csv")
print(df.head(3))
Age=df["Age"]

print("Age of the first 3 passengers: ",Age.head(3))

# get the each passenger's age one by one 
print("Average age of the passengers: ",Age.mean())