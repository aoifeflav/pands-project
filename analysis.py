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

#aesthetic plotting
import seaborn as sns

# Load the dataset
df = pd.read_csv("iris.csv")



#take a look
print(df.head())



# Create a bar chart showing how many of each species there are
#count how many of each species there are
species_amount = df['species'].value_counts()

#put it in a bar chart
plt.figure(figsize=(10, 6)) # make it bigger
species_amount.plot(kind = 'bar', color = ['#e39ff6', '#2c041c', '#710193'], edgecolor='black')
plt.ylabel("No. of Flowers Spotted") 
plt.xlabel("Species")
plt.xticks(rotation=0) #straighten bottom labels
plt.title("Amount of each Species Spotted")
plt.gca().spines['top'].set_visible(False) #remove line a top
plt.gca().spines['right'].set_visible(False) # remove line on right



#make a histogram for sepal length
sepal_length = df['sepal_length']

plt.figure(figsize=(10, 6)) # make it bigger
plt.hist(sepal_length, color='#9867c5', bins=20, edgecolor='black',)
plt.xlabel('Sepal Length (Cm)')
plt.ylabel('Frequency')
plt.title('Sepal Length')
plt.gca().spines['top'].set_visible(False) #remove line on top
plt.gca().spines['right'].set_visible(False) #remove line on right


#sepal width
sepal_width = df['sepal_width']

plt.figure(figsize=(10, 6)) # make it bigger
plt.hist(sepal_width, color='#be93d4', bins=20, edgecolor='black',)
plt.xlabel('Sepal Width (Cm)')
plt.ylabel('Frequency')
plt.title('Sepal Width')
plt.gca().spines['top'].set_visible(False) #remove line on top
plt.gca().spines['right'].set_visible(False) #remove line on right



#petal length
petal_length = df['petal_length']

plt.figure(figsize=(10, 6)) # make it bigger
plt.hist(petal_length, color='#311432', bins=20, edgecolor='black',)
plt.xlabel('Petal Length (Cm)')
plt.ylabel('Frequency')
plt.title('Petal Length')
plt.gca().spines['top'].set_visible(False) #remove line on top
plt.gca().spines['right'].set_visible(False) #remove line on right


#petal width
petal_width = df['petal_width']

plt.figure(figsize=(10, 6)) # make it bigger
plt.hist(petal_width, color='#7a4988', bins=20, edgecolor='black',)
plt.xlabel('Petal Width (Cm)')
plt.ylabel('Frequency')
plt.title('Petal Width')
plt.gca().spines['top'].set_visible(False) #remove line on top
plt.gca().spines['right'].set_visible(False) #remove line on right


# get the petal + sepal length and width from the data and name them as variables
plen = df['petal_length']
pwidth = df['petal_width']
slen = df['sepal_length']
swidth = df['sepal_width']


custom_colors=["#e39ff6", "#2c041c", "#710193"]

#1 Plot petal length vs petal width


#create plot
sns.scatterplot(x=plen, y=pwidth, hue="species", palette= custom_colors, alpha=0.7, data=df)

# Add labels and title
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width")
plt.grid(True)
plt.legend()



#2 Plot petal length vs sepal length

#create plot
sns.scatterplot(x=plen, y=slen, hue="species", palette= custom_colors, alpha=0.7, data=df)

# Add labels and title
plt.xlabel("Petal Length (cm)")
plt.ylabel("Sepal Length (cm)")
plt.title("Petal Length vs Sepal Length")
plt.grid(True)
plt.legend()



#3 Plot petal length vs sepal width
#create plot
sns.scatterplot(x=plen, y=swidth, hue="species", palette= custom_colors, alpha=0.7, data=df)

# Add labels and title
plt.xlabel("Petal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Petal Length vs Sepal Width")
plt.grid(True)
plt.legend()



#4 Plot petal width vs sepal length
#create plot
sns.scatterplot(x=pwidth, y=slen, hue="species", palette= custom_colors, alpha=0.7, data=df)

# Add labels and title
plt.xlabel("Petal Width (cm)")
plt.ylabel("Sepal Length (cm)")
plt.title("Petal Width vs Sepal Length")
plt.grid(True)
plt.legend()


#5 Plot petal width vs sepal width
#create plot
sns.scatterplot(x=pwidth, y=swidth, hue="species", palette= custom_colors, alpha=0.7, data=df)

# Add labels and title
plt.xlabel("Petal Width (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Petal Width vs Sepal Width")
plt.grid(True)
plt.legend()


#6 Plot sepal length vs sepal width
#create plot
sns.scatterplot(x=slen, y=swidth, hue="species", palette= custom_colors, alpha=0.7, data=df)

# Add labels and title
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width")
plt.grid(True)
plt.legend()



#output a summary of each variable to a single text file 
# Use  pandas . describe()
#To put all of them into the same file I should use a loop

#create a text file to write the summaries into
with open("variable_summary.txt", "w") as file:

  #Use for loop to iterate over each column and write their description into a text file
  for column in df.columns:
        file.write(f"Summary for {column}:\n")
        file.write(str(df[column].describe()) + "\n\n") 
#If run multiple times this will overwrite what is already written in the file rather than create duplicates of files


#The following plot just puts all of these together to be looked at side by side
sns.pairplot(df, hue='species',  palette= custom_colors, height=2)

plt.tight_layout()



#Create a boxplot of the three species and their distribution
#Exclude species
numerical_variables = df.columns[:-1]

# Set up plotting layout
plt.figure(figsize=(15, 5))

# Create boxplots
species = ['versicolor', 'setosa', 'virginica']
colors = ['#2c041c', '#e39ff6', '#710193'] 
for i,  specie in enumerate(species, start=1):
    plt.subplot(1, 3, i)
    plt.boxplot([df[df['species'] == specie][col] for col in numerical_variables],
                patch_artist=True,  #Enable filled boxplots
                boxprops=dict(facecolor=colors[i - 1]),  #box colour
                whiskerprops=dict(color='black'),  #whiskers colour
                capprops=dict(color='black'),  #caps colour
                medianprops=dict(color='black'),  #median line colour
                meanprops=dict(marker='o', markerfacecolor='black', markeredgecolor='black')  # Set style of mean marker
                )
    plt.xticks(range(1, len(numerical_variables) + 1), numerical_variables, rotation=45)
    plt.title(specie)

plt.tight_layout()



#define as a function
def graph(y): 
    colours = ['#e39ff6', '#2c041c', '#710193'] 
    sns.boxplot(x="species", y=y, data=df, palette=colours, flierprops=dict(marker='o', markersize=8, markerfacecolor='red', markeredgecolor='black'))
  
plt.figure(figsize=(10,10)) 
      
# Adding the subplot at the specified 
# grid position 
plt.subplot(221) 
graph('sepal_length') 
  
plt.subplot(222) 
graph('sepal_width') 
  
plt.subplot(223) 
graph('petal_length') 
  
plt.subplot(224) 
graph('petal_width') 
  



#Create a heatmap of the petal and sepal variables to find the correlation.

#first drop the species variable
heatmap_data = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]

# Calculate the correlation matrix
correlation = heatmap_data.corr()

# Create a heatmap using seaborn
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Iris Flower Heatmap")

