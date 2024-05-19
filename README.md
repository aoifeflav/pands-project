# Iris Dataset Analysis
### by Aoife Flavin 
---
This repository contains my analysis of the Iris dataset. The purpose of this repoitory is for my final project in the module Programming and Scripting, in Semester 1 of the Higher Diploma in Data Analytics at ATU.
---
## About the Iris dataset
The Iris dataset is a very commonly used dataset in the world of data science. It has been called the "Hello World of data science". The data is also sometimes known as  Fisher's Iris data set, after the biologist and statistician Ronald Fisher used it in his who used it in his 1936 paper 'The use of multiple measurements in taxonomic problems'.

The data set has 50 samples each of three different species of Iris; Iris Setosa, Iris Virginica and Iris Versicolor.

![Plot Image](iris_species.jpeg)

Source: Kaggle


The dataset contains five columns:
* Sepal Length 
* Sepal Width
* Petal Length
* Petal Width
* Species

The following image displays the difference between the petal and the sepal in an Iris flower.

![Plot Image](petal_and_sepal_dimensions.jpeg)

Source: Kaggle

## Exploratory Analysis
To begin my analysis I began by performing a count of each of the datatpoints in the variable 'species'. I then represented this data in a bar chart. As can be seen from the figure below, there is an even amount of data points for each species.

![Plot Image](bar_chart_flowers_spotted.png)


---
Following on from this I took a look at the statistical summary data of each of the variables, finding the mean, standard deviation, interquartile range and other data points to begin to understand the data. This summary data can be found [here.](variable_summary.txt)

In order to visualise the distribution of the individual variables I created four histograms.

### Sepal Length
![Plot Image](hist_slen.png)

This variable appears to be normally distributed, which is backed up by the statistical data, which puts the standard deviation at approxiately 14% of the mean. The standard deviation of this data is 0.828066, suggesting that throughout the sample data the length of sepals are close to the average length.

### Sepal Width
![Plot Image](hist_swidth.png)

Similarly to Sepal Length, Sepal width also appears to be normally distributed, which is backed up by the statistical data, putting the standard deviation at approxiately 14% of the mean. The standard deviation of 0.435866 suggests that across the samples the length of sepals are not far off the average width.

### Petal Length
![Plot Image](hist_plen.png)

Petal Length, on the other hand, appears to be bimodally distributed. The standard deviation of approximately 1.765298 (around 47% of the mean) suggests a higher level of variability amongst the data. There appears to be a smaller cluster of data skewed to the right, which could be explained by one of the species of Iris having significantly smaller petals than the others.

### Petal Width
![Plot Image](hist_pwidth.png)

Similarly to Petal Length, Petal width is also bimodally distributed. It again has a relatively high standard deviation of 0.762238 (about 63% of the mean) suggesting a higher variability amongst the data.




### Correlation of heatmap

This heatmap shows the pairwise correlation coefficients between the numeric variables giving a clearer picure of how features are related to eachother.
This is what the heatmap tells us about thecorrelation of variables:
* Petal length and width are very highly correlated
* Petal length and sepal length are also strongly correlation
* Similarly, Petal width and Sepal Length are highly correlated.
* The varables with the lowest correlation are Sepal width and Sepal length.





### MVP Project plan
Get these tasks done by 12/05 and from there add extras
* ~~create repository~~
* Write a summary of the dataset in the readme
* ~~Download dataset & add to repository (done in Ian's lectures)~~
* ~~have analysis.py output a summary of each variable to a single text file (extracting the result of pandas . describe() of each variable to a txt file.)~~ (Need to test)
* ~~Create a histrgram of sepal length~~
* ~~Create a histrgram of sepal width~~
* ~~Create a histrgram of petal length~~
* ~~Create a histrgram of petal width~~
* ~~Create a bar chart of flower type~~
* ~~Create a scatter plot of sepal length x width~~
* ~~Create a scater plot of petal length x width~~
* ~~Create a scater plot of petal length x sepal width~~
* ~~Create a scater plot of petal length x sepal length~~
* ~~Create a scatter plot of petal width x sepal width~~
* ~~Create a scatter plot of petal width x sepal length~~
### Improved Project plan
Aim to complete by 19/20 so there is time for final touches
* ~~Convert these plots to seaborn, so they can be viewed together with the different species seperated by~~ colour
* ~~Add a boxplot chage colours to purple and explain it's significance#~~
* Do some distplots (check the geek4geek source for how to do)
* Add in some mathematical bits about correlation
* ~~Use heatmaps to explai correlation (use geeks4geeks source)~~
* Insert all of the images of the plots created into the readme with a clear narrative

## Sources
https://en.wikipedia.org/wiki/Iris_flower_data_set#:~:text=The%20Iris%20flower%20data%20set,example%20of%20linear%20discriminant%20analysis.

https://github.com/mwaskom/seaborn-data/blob/master/iris.csv

Ian's lecture notes as a source

https://www.projectpro.io/recipes/write-text-file-output-of-for-loop

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/ --> V good source

https://github.com/abhikumar22/Exploratory-Data-Analysis-on-IRIS-Dataset/blob/master/EDA_Flower.ipynb

https://www.youtube.com/watch?v=02BFXhPQWHQ --> Vid of anaylsis that doesn't use seaborn

https://www.kaggle.com/datasets/uciml/iris

https://towardsdatascience.com/create-and-customize-boxplots-with-pythons-matplotlib-to-get-lots-of-insights-from-your-data-d561c9883643 --> Boxplots

https://www.simplypsychology.org/boxplots.html

https://medium.com/@hfahmida/eda-for-iris-dataset-with-boxplots-violin-plots-heatmap-pairwise-plots-535275b4c2a0#:~:text=The%20correlation%20heatmap%20shows%20the,sepal%20length%20and%20petal%20length.

https://zion-oladiran.medium.com/exploratory-data-analysis-iris-dataset-68897497b120 --> another good source for explaining boxplots