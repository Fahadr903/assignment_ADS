"""
@author: Md Fahadur Rahman Chowdhury
"""

#import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# deefine line plot function
def line_plot(df, labels):
    
    """ This function s for line plot
    
    """
    
    plt.figure()
    
    # plot
    for label in labels:
        plt.plot(df['Time'], df[label], label = label)
        
        
    # remove whitespace
    plt.xlim(min(df["Time"]), df["Time"].max())
    
    # set label, legend
    plt.xlabel("Year")
    plt.ylabel("GDP per capita")
    
    plt.legend()
    
    # save
    plt.savefig('line.png')
    
    plt.show()
    
    return


#define bar plot function
def bar(df):
    """
    This function is for bar plot
    """
    
    plt.figure()
    
    plt.bar(df['Time'], df['Population, male'], label = "Male")
    plt.bar(df['Time'], df['Population, female'], bottom = df['Population, male'], label = "Female")
    
    #set label and legend
    plt.xlabel("Time")
    plt.ylabel("Population")
    
    plt.legend()
    
    # save
    plt.savefig('bar.png')
    
    plt.show()
    return


#define pie plot function
def pie(df, labels):
    
    """ This function is for pie chart."""
    
    plt.figure()
    
    for label in labels:
        plt.pie(df['Forest area'], labels = labels)
        
    # save
    plt.savefig('pie.png')
    
    plt.show()
    
#read file
population = pd.read_csv('population.csv')

# call line_plot
line_plot(population, ['China [CHN]','India [IND]', 'Germany [DEU]','South Africa [ZAF]'])


# read file
china = pd.read_csv("china.csv")

# call bar function
bar(china)

# read file
area = pd.read_csv('area.csv')

#print()
# call pie
pie(area, list(area['Country Name']))