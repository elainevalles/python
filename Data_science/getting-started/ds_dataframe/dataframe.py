import pandas as pd

d = {'col1': [32, 34, 29, 28, 49],
	 'col2': [34, 11, 35, 29, 21],
	 'col3': [19, 33, 49, 22, 31]}

df = pd.DataFrame(data=d)

print(df)
