# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:02:38 2023

Midterm 
"""




def update_dict(main_dict, delta_dict):
    """
    Define a function update_dict() that takes as arguments two dictionaries,
main_dict and delta_dict, both of which have strings as the values associated with their
keys. Dictionary delta_dict contains data for updating main_dict. Update main_dict in
place: do not explicitly return a value.
Consider a key k that is in delta_dict and let v be the value of delta_dict[k]. If k is not in
main_dict, add to main_dict an element with key k and value v. If key k is in main_dict
and v is the empty string, then delete k (and its associated value) from main_dict. Finally, if k
is in main_dict but v is some string other than the empty string, then change the value
associated with k in main_dict to the value v

    Parameters
    ----------
    main_dict : TYPE
        DESCRIPTION.
    delta_dict : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    for k, v in delta_dict.items():
        if k in main_dict:
            if v:
                main_dict[k] = v
            else:
                del main_dict[k]
        else:
            main_dict[k] = v
            
class Pet():
    """
    Define classes Pet and Cat where Cat is derived from Pet. Pet has one instance
attribute, name (the name of the pet); when called, the name (a string) is passed. When an
instance of Pet occurs in a position where a string is expected, it is replaced by the value of the
name attribute.
    """
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'{self.name}'
    #can also use -> return self.name
    

class Cat(Pet):
    """
    Cat has two instance attributes: name (as with Cat) and mice_caught, an integer denoting the
number of mice the cat has caught. When Cat is called, values for these two attributes are
passed. Cat inherits the __str__() method from Pet. It has a catch_mice() method, which
is passed the number of mice the cat caught in its last expedition. If this number is less than 1,
raise a ValueError exception with the text 'Must catch at least 1 mouse', and otherwise update the 
value of the mice_caught attribute by adding to it the number of mice just caught.
    """
    def __init__(self, name, mice_caught: int):
        # inherit __str__() method from Pet
        Pet.__init__(self, name)
        self.mice_caught = mice_caught
    
    def catch_mice(self, numofmice):
        if numofmice < 1:
            raise ValueError('Must catch at least 1 mouse')
        self.mice_caught  += numofmice
        
        return numofmice

import re

def match_gpa(st):
    """
    Define a Python function match_gpa() that is passed a string that is supposed to
contain a person’s first name followed (after some whitespace) by their GPA with three digits
after the decimal point. It checks that the string is matched by a regex-defined pattern that
captures two groups: the name and the GPA. The pattern for the name is a capital letter followed
by one or more lowercase letters. The pattern for the GPA is a digit between 0 and 3 (inclusive),
followed by a decimal point, followed by three digits. (We don’t expect anyone to have a 4.0
GPA.) There is any amount of whitespace but nothing else before the name, and any amount of
whitespace but nothing else after the GPA. ) If the string passed in is matched by the pattern, 
then the function returns a string of the form <name>, GPA is <GPA> where <name> is the string 
matching the name pattern, and <GPA> is the string matching the GPA pattern. If the string is not
matched by the pattern, then the function returns a string of the form Invalid format: <st> where
<st> is the string that was passed in
    """
    regex = re.compile(r'^\s*([A-Z][a-z]+)\s+([0-3]\.\d{3})\s*$')
    match= regex.search(st)
    
    if match:
        return f'{match.group(1)}, GPA is {match.group(2)}'
    return f'Invalid format: {st}'        
            
        



if __name__ == '__main__':

    m_dict = {'a':'dog', 'b':'cat', 'd':'fox', 'e':'hen'}

    d_dict = {'b':'mouse', 'c':'rat', 'e':''}

    update_dict(m_dict, d_dict)

    print(m_dict)
    
    rover = Pet('Rover')

    print(rover)

    felix = Cat('Felix', 3)

    felix.catch_mice(2)

    print(felix, felix.mice_caught)

    try:

        felix.catch_mice(0)

    except ValueError as detail:

        print(detail)
    
    print(match_gpa('Allen 2.521'))

    print(match_gpa(' Tyler   3.651  '))

    print(match_gpa('George 2.32'))

    print(match_gpa('Alexis = 3.545'))

    print(match_gpa('Ed  2.965  x'))
