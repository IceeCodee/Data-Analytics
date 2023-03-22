import sqlite3
import typing

def create_database():
    """Create a database 
    
    Function create_database() makes a connection to mydatabase.db, 
    creates a cursor, and makes a table mytable with columns name (type TEXT) and age (type 
    INTEGER). It populates the table with data from file students.txt 
    """
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()

    sql_command = """
    CREATE TABLE mytable (
        name VARCHAR(20),
        age INT(2)            
        );
    
    """
    cursor.execute(sql_command)

    with open('students.txt') as file:
        for line in file:
            name, age = line.strip().split(',')
            insert_command = """
                INSERT INTO mytable (name, age) VALUES (?, ?);
                """
            cursor.execute(insert_command, (name, int(age)))

    connection.commit()
    connection.close()


def students_of_age(years_old: int):
    """Finds the names of students with given age in the students file
    
    Function students_of_age(years_old), where years_old is an integer (age in years), 
    returns a list of the names of the students whose age is years_old.

    ARGS:
        years_old: the age in years to search for in the database
        
    RETURNS:
        res: a list of names of students whose age is determined by years_old variable
    """
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    
    age_command = """
    SELECT name FROM mytable
    WHERE age = ?;
    """
    cursor.execute(age_command, (years_old,))
    res = [name[0] for name in cursor.fetchall()]

    connection.commit()
    connection.close()

    return res


def average_age() -> float:
    """Finds the average age of all entries in student file
    
    Function average_age() returns the average of the values in the age column of mytable

    ARGS:
        none
        
    RETURNS:
        avg_age: the average age of all students in the database rounded to 2 decimal points
    """
    connection = sqlite3.connect('mydatabase.db')
    cursor = connection.cursor()
    
    average_command = """
    SELECT age FROM mytable;
    """
    cursor.execute(average_command)
    ages = [age[0] for age in cursor.fetchall()]
    avg_age = sum(ages) / len(ages)

    connection.commit()
    connection.close()

    return round(avg_age, 2)

if __name__ == '__main__': 
 create_database() 
 print(students_of_age(26)) 
 print(f'{average_age():.2f}') 
