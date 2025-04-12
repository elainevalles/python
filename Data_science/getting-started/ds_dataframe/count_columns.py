import pandas as pd

d = {'col1': [32, 34, 29, 28, 49],
	 'col2': [34, 11, 35, 29, 21],
	 'col3': [19, 33, 49, 22, 31]}

df = pd.DataFrame(data=d)
count_column = df.shape[1]
count_rows = df.shape[0]

print("Number of columns: ")
print(count_column)
print("Number of rows: ")
print(count_rows)
