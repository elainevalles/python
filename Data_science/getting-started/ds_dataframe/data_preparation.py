import pandas as pd

path = "/home/eparra-v/Documents/Python/Data_science/getting-started/ds_dataframe/data.csv"
health_data = pd.read_csv(path, header=0, sep=",")

#dropna() function to remove the NaNs. axis=0 means that we want to remove all rows that have a NaN value
health_data.dropna(axis=0, inplace=True)
print(health_data)

# Tip: If you have a large CSV file, you can use the head() function to only show the top 5rows:5
# print(health_data.head())

#info() function to list the data types within our data set:
print(health_data.info())

#astype() function to convert the data into float64.
health_data["Average_Pulse"] = health_data['Average_Pulse'].astype(float)
health_data["Max_Pulse"] = health_data['Max_Pulse'].astype(float)
print("After astype() application parsing it to float")
print(health_data.info())