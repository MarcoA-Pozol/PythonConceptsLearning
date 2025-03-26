"""
	System that checks the student qualification in different subjects and return an average note.
    Checks if student aproved or not.
    
    We are using 'if' conditional.
"""

notes_dict = {
	'Advanced Topics of Programming I': 9.7,
    'Object Oriented Programming II': 5.4,
    'Software Engineering I': 6.5,
    'Database Management III': 8.6,
    'Networks II': 9.3,
}

def get_user_note(notes_dict:dict) -> float:
    """
        Obtain the average note with a sum of every note and dividing by the number of subjects.
        
        Attributes:
            - notes_dict(dict): Dict of notes as subjects as keys and notes as values.
            
        Returns:
            - result(float): The average final note of all the user's subjects notes.
    """
    
    result = 0
	# Validate every note in the dictionary.
    for value in notes_dict.values():
        result += value
        
    result = result / len(notes_dict)
    
    return result
            
            
def comprobe_if_user_aproved(function=get_user_note(notes_dict)) -> bool:
    if function < 7:
        return False
    return True

print(f'Note: {get_user_note(notes_dict)}')
print("Aproved") if comprobe_if_user_aproved() == True else print("Not Aproved")