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


# get the petal + sepal length and width from the data and name them as variables
plen = df['petal_length']
pwidth = df['petal_width']
slen = df['sepal_length']
swidth = df['sepal_width']

#1 Plot petal length vs petal width

#Use the stateful approach
fig, ax = plt.subplots(figsize=(10,6))

#plot it and make it pretty
ax.scatter(plen, pwidth, color='orange', alpha=0.6, s=80, edgecolor='black')
ax.set_xlabel('Petal Length', fontsize=12)
ax.set_ylabel('Petal Width', fontsize=12)
ax.set_title('Petal Length vs Petal Width', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7) #add graph lines
ax.tick_params(axis='x',labelsize=10)
ax.tick_params(axis='y',labelsize=10)
fig.tight_layout()




#2 Plot petal length vs sepal length

#Use the stateful approach
fig, ax = plt.subplots(figsize=(10,6))

#plot it and make it pretty
ax.scatter(plen, slen, color='orange', alpha=0.6, s=80, edgecolor='black')
ax.set_xlabel('Petal Length', fontsize=12)
ax.set_ylabel('Sepal Length', fontsize=12)
ax.set_title('Petal Length vs Sepal Length', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7) #add graph lines
ax.tick_params(axis='x',labelsize=10)
ax.tick_params(axis='y',labelsize=10)
fig.tight_layout()



#3 Plot petal length vs sepal width

#Use the stateful approach
fig, ax = plt.subplots(figsize=(10,6))

#plot it and make it pretty
ax.scatter(plen, swidth, color='orange', alpha=0.6, s=80, edgecolor='black')
ax.set_xlabel('Petal Length', fontsize=12)
ax.set_ylabel('Sepal Width', fontsize=12)
ax.set_title('Petal Length vs Sepal Width', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7) #add graph lines
ax.tick_params(axis='x',labelsize=10)
ax.tick_params(axis='y',labelsize=10)
fig.tight_layout()



#4 Plot petal width vs sepal length

#Use the stateful approach
fig, ax = plt.subplots(figsize=(10,6))

#plot it and make it pretty
ax.scatter(pwidth, slen, color='orange', alpha=0.6, s=80, edgecolor='black')
ax.set_xlabel('Petal Width', fontsize=12)
ax.set_ylabel('Sepal Length', fontsize=12)
ax.set_title('Petal Width vs Sepal Length', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7) #add graph lines
ax.tick_params(axis='x',labelsize=10)
ax.tick_params(axis='y',labelsize=10)
fig.tight_layout()



#5 Plot petal width vs sepal width

#Use the stateful approach
fig, ax = plt.subplots(figsize=(10,6))

#plot it and make it pretty
ax.scatter(pwidth, swidth, color='orange', alpha=0.6, s=80, edgecolor='black')
ax.set_xlabel('Petal Width', fontsize=12)
ax.set_ylabel('Sepal Width', fontsize=12)
ax.set_title('Petal Width vs Sepal Width', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7) #add graph lines
ax.tick_params(axis='x',labelsize=10)
ax.tick_params(axis='y',labelsize=10)
fig.tight_layout()



#6 Plot sepal length vs sepal width

#Use the stateful approach
fig, ax = plt.subplots(figsize=(10,6))

#plot it and make it pretty
ax.scatter(slen, swidth, color='orange', alpha=0.6, s=80, edgecolor='black')
ax.set_xlabel('Sepal Length', fontsize=12)
ax.set_ylabel('Sepal Width', fontsize=12)
ax.set_title('Sepal Length vs Sepal Width', fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7) #add graph lines
ax.tick_params(axis='x',labelsize=10)
ax.tick_params(axis='y',labelsize=10)
fig.tight_layout()

plt.show()