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


'''
# Create a bar chart showing how many of each species there are
#count how many of each species there are
species_amount = df['species'].value_counts()

#put it in a bar chart
plt.figure(figsize=(10, 6)) # make it bigger
species_amount.plot(kind = 'bar', color = ['#a32cc4', '#b65fcf', '#e39ff6'], edgecolor='black')
plt.ylabel("No. of Flowers Spotted") 
plt.xlabel("Species")
plt.xticks(rotation=0) #straighten bottom labels
plt.title("Amount of each Species Spotted")
plt.gca().spines['top'].set_visible(False) #remove line a top
plt.gca().spines['right'].set_visible(False) # reove line on right
'''


#make a histogram for sepal length
sepal_length = df['sepal_length']

plt.figure(figsize=(10, 6)) # make it bigger
plt.hist(sepal_length, color='#9867c5', bins=20, edgecolor='black',)
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.title('Sepal Length')
plt.gca().spines['top'].set_visible(False) #remove line on top
plt.gca().spines['right'].set_visible(False) #remove line on right


#sepal width
sepal_width = df['sepal_width']

plt.figure(figsize=(10, 6)) # make it bigger
plt.hist(sepal_width, color='#be93d4', bins=20, edgecolor='black',)
plt.xlabel('Sepal Width')
plt.ylabel('Frequency')
plt.title('Sepal Width')
plt.gca().spines['top'].set_visible(False) #remove line on top
plt.gca().spines['right'].set_visible(False) #remove line on right


#petal length
petal_length = df['petal_length']

plt.figure(figsize=(10, 6)) # make it bigger
plt.hist(petal_length, color='#311432', bins=20, edgecolor='black',)
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.title('Petal Length')
plt.gca().spines['top'].set_visible(False) #remove line on top
plt.gca().spines['right'].set_visible(False) #remove line on right



#petal width
petal_width = df['petal_width']

plt.figure(figsize=(10, 6)) # make it bigger
plt.hist(petal_width, color='#7a4988', bins=20, edgecolor='black',)
plt.xlabel('Petal Width')
plt.ylabel('Frequency')
plt.title('Petal Width')
plt.gca().spines['top'].set_visible(False) #remove line on top
plt.gca().spines['right'].set_visible(False) #remove line on right

plt.show()

'''
plen = df['petal_length']
'''