"""
	Lambda Function (Anonymous Function): A function that executes only one time while is defined, it´s about having just one line of code, ideal for those events are not going to be called again.
""" 

# Normal function.
def sum_numbers(a, b):
	"""
		Returns the sum of a + b as a result.
	"""
	return a + b
	
print(f'Normal function: {sum_numbers(5, 10)}')
	
# Lambda function structure.
# Lambda functions have an implicit 'return' statement, we do not have explicit return something.
# name_of_the_function(optional) lambda argument1, argument2:(functionality).
# Example of lambda function.
sum_numbers = lambda a, b: a + b

print(f'Lambda function: {sum_numbers(5, 10)}')


""" 
    Both normal and lambda functions do the same, but lambda is most suitable for this simple case, resuming the lines of code we have to write down.
    
    From:
    def sum_numbers(a, b):
        return a + b
    
    To:
    sum_numbers = lambda a, b: a + b
"""
