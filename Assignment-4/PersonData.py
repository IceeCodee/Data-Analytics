"""


@author: taylor headen 
COMP 651
Assignment 4 question 1

"""

class PersonData:
    
    """
    This module lets us find the data of a given person
    
    An instance has a persons age, number of children and spouse's name and
    returns all the information
    
    Attributes:
        age (number in years) the persons current age
        children (number) the amount of children the perons has
        spouse (string) the name of the person's spouse
        
    Methods:
        __init__(): initializes person data
        __str__(): prints out the age of the person
        birthday(): increments person age by 1
        new_child(): increments the number of children the person has by 1
        print_data(): returns the person's data
        marries(): adds a record of the spouse given that one does not already exist
        divorces(): delets the record of the spouse given a spouse exists
    """
    def __init__(self, age, spouse = 'None', children =0 ):
        """"Called: PersonData(age, spouse, children)"""
        self.age = age
        self.spouse = spouse
        self.children = children
    
    def __str__(self):
        """Returns the age of ther person """
        return f'A {self.age} year old person'
        
    def birthday(self):
        """Increments persons age"""
        #do not have to return just self.age +=1 will suffice
        
        self.age = self.age + 1
        return self.age 
    
    
    def new_child(self):
        """Increments the number of children the person has"""
        #do not have to return just self.children +=1 will suffice

        self.children = self.children + 1
        return self.children 
    
    def print_data(self):
        """Prints the person data"""
        #Reserve two character positions for integer values
        #that are the values of the age and children attributes, and leave plenty of space
        #between the values.Note whitespace
        #0,1,2 represents age,children,spouse respectively
        print("{0:2d}     {1:2d}     {2:s}".format(
              self.age, self.children, 
              self.spouse if hasattr(self, "spouse") else "None"))
            
    def marries(self, spouse):
        """Updates spouse name"""
        if not hasattr(self, 'spouse'):
           self.spouse = spouse
         #use raise Exception 
        else:
            print(f'Spouse exists: {self.spouse}')
            
    def divorces(self):
        """Removes spouse name"""
        "if statement"
        if hasattr(self, 'spouse'):
            del self.spouse
            #raise AttributeError
        else:
            print("Not married, divorce impossible")
        

class EmployedPersonData(PersonData):
    
    """This module lets us find the data of a given person
    
    An instance has a persons age, number of children and spouse's name and employer. It then
    returns all the information
    
    Subclass of:
        PersonData: add attribute employer (the compnay in which the person is employeed by), 
        extends __init__() to include employer, overrides print_data()
    
    Attributes:
        age (number in years) from PersonData: the persons current age
        children (number) from PersonData: the amount of children the perons has
        spouse (string) from PersonData: the name of the person's spouse
        
    """
    def __init__(self, age, employer , spouse='None', children=0):
        """Calls init method from PersonData class"""
        PersonData.__init__(self, age, spouse, children)
        self.employer = employer
    
    def __str__(self):
        """Returns age of person and their employer"""
        return f'A {self.age} year old person employed by {self.employer}'
           
    def print_data(self):
        """Prints the person data now including the employer"""
        #formatted better
        print("{0:2d}     {1:2d}     {2:s}     {3:s}".format(
        self.age, self.children, self.employer,
         self.spouse if hasattr(self, "spouse") else "None"))

        
if __name__=="__main__":
    
    p1 = PersonData(31, spouse="Sue", children=2)
    print(p1)
    p1.print_data()
    p1.birthday()
    p1.new_child()
    p1.divorces()
    p1.print_data()
    p1.marries("Pam")
    try:
        p1.marries("Sue")
    except Exception as detail:
        print(detail)
    try:
        p1.divorces()
        p1.divorces()
    except AttributeError as detail:
        print(detail)
    p2 = PersonData(39)
    p2.print_data()
    ep1 = EmployedPersonData(31, "Google", spouse="Tom", children=3)
    print(ep1)
    ep1.print_data()

