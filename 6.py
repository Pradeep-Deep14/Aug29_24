#import numpy as np
#import pandas as pd


#Importing and Reading the file.

#input_file = "G:\Python\Aug 29_24\csv file.csv"

#dataframe=pd.read_csv("G:\Python\Aug 29_24\csv file.csv")
#Handling the null values and cleaning

#df= fill.na("Current_Date")

#Drop null values

#dataframe = pd.drop(Date='01.08.2029', inplace = True)

#Transformation in Date part

#output_file=pd.dataframe
#print(dataframe)

import numpy as np
import pandas as pd
from datetime import datetime

# Importing and reading the file
input_file = "G:\\Python\\Aug 29_24\\csv file.csv"

# Reading the CSV into a DataFrame
dataframe = pd.read_csv(input_file)

# Replacing 'na' with the current date
current_date = datetime.now().strftime('%d.%m.%Y')
dataframe['Date'] = dataframe['Date'].replace('na', current_date)

# Dropping rows where the date is '01.08.2029'
dataframe = dataframe[dataframe['Date'] != '01.08.2029']

# Converting the Date column to datetime format
dataframe['Date'] = pd.to_datetime(dataframe['Date'], format='%d.%m.%Y')

# Printing the cleaned and transformed DataFrame
print(dataframe)
