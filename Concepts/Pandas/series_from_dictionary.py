"""
	Series from Pandas using a dictionary for indexes and values.
	
	When using a dict with a series data structure, the dictionary keys become the indexes.
"""
import pandas as pd


# Dataset
users = {
    'first_name': ['Andrew', 'Jennifer', 'Tomas', 'Pedro', 'Fer'],
    'last_name': ['Reynolds', 'Laurance', 'Garcia', 'Mendez', 'Hardy'],
    'age': [19, 40, 29, 35, 52]
}

series = pd.Series(users)

print(series)