import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# os.chdir(r"E:\IBI资料\practical相关\IBI1_2025-26\IBI1_2025-26\Practical10")
# os.listdir()
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# print(dalys_data.head(5))
# dalys_data.info()
# print(dalys_data.describe())
# print(dalys_data.iloc[0,3])
# print(dalys_data.loc[0, "DALYs"])
# print(dalys_data.iloc[2,0:5])
# print(dalys_data.iloc[0:2,:])
# print(dalys_data.iloc[0:10:2,0:5])

# print the third and fourth columns (the year and the DALYs) for the first 10 rows (inclusive)
print(dalys_data.iloc[0:10,2:4])

# filter all the rows of Afghanistan and store them in a new dataframe
# take out the first 10 lines
# find the line number where the max DALYs is located
# find the year according to that line number
afg = dalys_data.loc[dalys_data["Entity"] == "Afghanistan"]
afg_10 = (afg.iloc[0:10, 2:4])
afg_max_year = afg_10.loc[afg_10["DALYs"].idxmax(), "Year"] # The largest DALYs occurred in 1998 in Afghanistan across the first 10 years.
print(f"The largest DALYs occurred in {afg_max_year} in Afghanistan across the first 10 years.")
# my_columns = [True, True, False, True]
# print(dalys_data.iloc[0:3,my_columns])

# create a variable to store a list of Booleans
# use this list to find the years of Zimbabwe
Zimbabwe_rows = dalys_data["Entity"] == "Zimbabwe"
Zimbabwe_years = dalys_data.loc[Zimbabwe_rows, "Year"]
print(Zimbabwe_years)

recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
recent_max_index = recent_data["DALYs"].idxmax()
recent_min_index = recent_data["DALYs"].idxmin()
recent_max_country = recent_data.loc[recent_max_index, "Entity"]
recent_min_country = recent_data.loc[recent_min_index, "Entity"]
recent_max_dalys = recent_data.loc[recent_max_index, "DALYs"]
recent_min_dalys = recent_data.loc[recent_min_index, "DALYs"]
print(recent_max_country)
print(recent_min_country)

sg = dalys_data.loc[dalys_data["Entity"] == "Singapore"]
plt.plot(sg.Year, sg.DALYs, 'g+') # The preceding letters represent colors, e.g., b for blue, r for red, g for green. The following symbols indicate the shape of the scatter points: + for a plus-shaped scatter plot, o for a circular scatter plot.
plt.xticks(sg.Year,rotation=-90) # Set the x-axis tick labels to the years and rotate them 90 degrees clockwise.
plt.tight_layout()
plt.xlabel("Year")
plt.ylabel("DALYs per year")
plt.title("DALYs in Singapore per year")
plt.show()

grouped = dalys_data.groupby("Year")
max_dalys = grouped["DALYs"].max()
min_dalys = grouped["DALYs"].min()
diff = max_dalys - min_dalys
plt.plot(diff.index, diff.values, 'b+')
plt.xlabel("Year")
plt.ylabel("DALYs gap (max - min)")
plt.title("Gap in DALYs between countries over time")
plt.xticks(rotation=-90)
plt.tight_layout()
plt.show()

print(dalys_data.loc[dalys_data["DALYs"].idxmax()]) # maximum occurred in Rwanda in 1994, with DALYs = 693367.49
print(dalys_data.loc[dalys_data["Year"] == 2010].sort_values("DALYs", ascending=False).head()) # maximum in 2010 occurred in Haiti, with DALYs = 184708.16