
# Read data from the external csv file

import pandas as pd

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("movieList.csv")

# This will display all the data in the csv file
# usually we get data from the external files

print(movies)



