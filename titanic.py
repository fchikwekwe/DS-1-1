# pure Python method
import csv

def did_female_survive(csv_file):
    counter = 0
    with open(csv_file) as file:
        titanic_file = csv.reader(file)
        for row in titanic_file:
            if row[1] == '1' and row[4] == 'female':
                counter += 1
    return counter

did_female_survive('titanic.csv')

# Pandas method
import pandas as pd

df = pd.read_csv('titanic.csv') # get pandas dataframe
df.head() # returns the first five rows or specified as param
df["Sex"] == "female" # get the female passengers
df[df["Sex" == "female"]] # slice of passengers where sex is female
df[(df["Sex"] == "female") && (df["Survived"] == 1)] # slice of passengers where they survived and are female
len(df[(df["Sex"] == "female") && (df["Survived"] == 1)] ) # get the count
