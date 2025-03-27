"""
	Pandas Series excel-like alphabethical index.
	
	When using a custom index, it´s neccesary to define every value of the index, this is ovewhelming, we can automate this with an
	index_generation function.
    
    Obtain custom indexes like "a, b, c, d...aa, ab, ac, ad....aaa, aab, aac, aad" automatically generated.
"""
import pandas as pd
import string

# Function that generates an alphabethical and autoincrementable list of indexes
def index_generation(n:int):
    """
    Generates an indexes list.
    
    Args:
        n (int): The number of indexes to generate.
        
    Returns:
        list: List of generated indexes.
	"""
    result = []
    i = 0
    while len(result) < n:
        name = ''
        num = i
        while True:
            name = string.ascii_lowercase[num % 26] + name
            num = num // 26 - 1
            if num < 0:
                break
        result.append(name)
        i += 1
        
    return result
    
# Pandas series object

weights = [70, 95, 68, 60, 87, 109, 84, 70, 92, 72, 69, 104, 95, 83, 87, 84, 78, 94, 78, 59, 73, 76, 98, 106, 78, 84, 102, 75, 82, 95, 99, 79, 88, 60]

weights_series = pd.Series(data=weights, index=index_generation(len(weights)))

print(weights_series)