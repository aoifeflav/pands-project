# Analysis.py
# This is my analysis of the Iris dataset
# Author: Aoife Flavin

#import libaries
#Data Frames
import pandas as pd

#numpy
import numpy as np

#plotting
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("iris.csv")

'''
#take a look
print(df.head())
'''

#count how many of each species there are
species_amount = df['species'].value_counts()

#put it in a bar chart
plt.figure(figsize=(10, 6)) # make it bigger
species_amount.plot(kind = 'bar', color = ['#F2C6DE', '#DBCDF0', '#C6DEF1'], edgecolor='black')
plt.ylabel("No. of Flowers Spotted") 
plt.xlabel("Species")
plt.xticks(rotation=0) #straighten bottom labels
plt.title("Amount of each Species Spotted")
plt.gca().spines['top'].set_visible(False) #remove line a top
plt.gca().spines['right'].set_visible(False) # reove line on right

plt.show()





'''
plen = df['petal_length']
'''