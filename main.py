# Pandas: Convert a DataFrame to a List of Dictionaries

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 3, 5, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

list_of_dicts = df.to_dict('records')

# [{'name': 'Alice', 'experience': 1, 'salary': 175.1}, {'name': 'Bobby', 'experience': 3, 'salary': 180.2}, {'name': 'Carl', 'experience': 5, 'salary': 190.3}, {'name': 'Dan', 'experience': 7, 'salary': 205.4}]
print(list_of_dicts)