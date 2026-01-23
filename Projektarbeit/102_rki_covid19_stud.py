# Angelehnt an Jupyter Notebook (https://jupyter.org/),
# Kaggle avocado data set (https://www.kaggle.com/mcamli/avocado) and
# For real RKI covid data see: https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/66876b81065340a4a48710b062319336/about

# Import and load necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

import warnings
warnings.filterwarnings("ignore")

# Jupyter Notebook simulation
# Alternative: from jupiter_module import continue_with
def continue_with(chapter):
    _input = input("\nContinue with " + chapter + " (Y/n/x)? (x for exit) ")
    if _input in ('Y', 'y', ''):
        print("\n")
        return True
    elif _input in ('X', 'x'):
        quit()
    else:
        return False

# MAIN
if __name__ == "__main__":

    #Load the dataset & display the first rows
    df_raw = pd.read_csv(r"D:\Lehre\Sem 1\Python\102_RKI_COVID19.csv")
    print(f"df_raw.head():\n{df_raw.head()}")

    if continue_with("data overview"):
        # Create an adequate data overview
        print ("Rows       : " ,df_raw.shape[0])
        print ("Columns    : " ,df_raw.shape[1])
        print ("\nFeatures : \n" ,df_raw.columns.tolist())
        print ("\nMissing values :  ", df_raw.isnull().sum().values.sum())
        print ("\nUnique values :  \n",df_raw.nunique())


    if continue_with("data description"):
        # Create an adequate data overview with available functions
        df_raw.describe()
        df_raw.info()


    if continue_with("exploratory data analysis"):
        ### Exploratory Data Analysis
        # Print Histogram of Dataframe for each column
        #A histogram is a great tool for quickly assessing a probability distribution that is intuitively understood by almost any audience.
        #Pandas hist() method is probably most convenient
        print(df_raw.hist(bins=25,figsize=(12,10),color='#86bf91'))
        dover = df_raw.hist(grid=1, bins=5, figsize=(20, 15), color='#009051', histtype="barstacked")
        plt.show() 


    if continue_with("data analysis: Neue Todesfälle"):
        # Ihr Code folgt hier ...
        pass


    if continue_with("data analysis: Baden-Württemberg"):
        # TBD: show all data specific to Bundesland Baden-Württemberg
        # using following hints  
        # https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
        # Ihr Code folgt hier ...
        pass