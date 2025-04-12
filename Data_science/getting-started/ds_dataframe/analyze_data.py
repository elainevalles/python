import pandas as pd

path = "/home/eparra-v/Documents/Python/Data_science/getting-started/ds_dataframe/data_two.csv"
health_data = pd.read_csv(path, header=0, sep=",")
pd.set_option('display.max_columns', None)
print(health_data.describe())
print('''

	Count - Counts the number of observations
	Mean - The average value
	Std - Standard deviation (explained in the statistics chapter)
	Min - The lowest value
	25%, 50% and 75% are percentiles (explained in the statistics chapter)
	Max - The highest value

	''')